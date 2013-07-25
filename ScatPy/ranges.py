# -*- coding: utf-8 -*-
"""
A collection of ranges found in ddscat.par


"""


from __future__ import division
import numpy as np


class How_Range():
    """
    A general range used for wavelength and aeff definitions.


    :param first: The first value of the range.
    :param last: The last value of the range.
    :param num: The number of steps in the range.
    :param how: An optional string defining the spacing of steps 'LIN', 'INV', 'LOG', 'TAB'.
                Default is 'LIN'.
    :param table: an optional list of table values that specify an arbitrary sequence.
    
    The range can be used as an iterator.        
    """
    def __init__(self, first, last, num, how=None, table=None):

        self.first=first
        self.last=last
        self.num=num
        self.how=how if how is not None else 'LIN'
        
        if self.how=='TAB':
            if self.tab is None:
                raise ValueError('TAB range requires table of values')
        self.build_table()

    def __str__(self):
        """ A string describing the range """
        return '%f  %f  %d  %s'%(self.first, self.last, self.num, self.how)
   
    def build_table(self):
        """ Build the internal representation of the points in the range """
        if self.how=='LIN':
            self.table=np.linspace(self.first, self.last, self.num)
        if self.how=='INV':
            l=self.table=np.linspace(1/self.first, 1/self.last, self.num)
            self.table=1/l
        if self.how=='LOG':
            self.table=np.logspace(np.log10(self.first), np.log10(self.last), self.num)

    def __iter__(self):
        self.build_table()
        self.current=0
        return self
    
    def next(self):
        if self.current==len(self.table):
            raise StopIteration
        
        self.current+=1
        return self.table[self.current-1]

    

class Lin_Range(How_Range):
    """
    A specialized linear range used for specifying target rotations.
    
    The range can be used as an iterator.    

    :param first: The first value of the range.
    :param last: The last value of the range.
    :param num: The number of steps in the range.
    """
    def __init__(self, first, last, num):
        How_Range.__init__(self, first, last, num, 'LIN')

    def __str__(self):
        """ A string describing the range """
        return '%f  %f  %d'%(self.first, self.last, self.num)

     
class Scat_Range():
    '''
    A specialist range used for specifying scattering planes.

    :param phi: The phi scattering angle.
    :param theta_min: The smallest value of theta.
    :param theta_max: The largest value of theta.
    :param d_theta: The theta stepsize.

    Cannot yet be used as an iterator    
    '''
    def __init__(self, phi, theta_min, theta_max, dtheta):

        self.phi=phi
        self.theta_min=theta_min
        self.theta_max=theta_max
        self.dtheta=dtheta

    def __str__(self):
        """ A string describing the range """
        return '%f  %f  %f  %s'%(self.phi, self.theta_min, self.theta_max, self.dtheta)

