import pyproj
import geocoder
import numpy as np
import utils.geo
import utils.coordinate

class FireLocalizer:
    def __init__(self):
        '''
        '''
        self.K = None
        self.R = None
        self.t = None
        self.init_elev = None
        self.height = None
        self.p = []

    '''
    @function: retrieve the height over the ground
    @param: none
    @output: the height of the current drone over the ground
    @TODO: adapt it such that we are not just using the initial elevation as the relative zero point
    '''
    def get_height(self):
        curr_elev = get_GPS()
        self.height = curr_elev - self.init_elev
        return self.height
    
    '''
    @function: 
    @param:
    @output:
    '''
    def get_position(self):
        pass
    
    def get_angle(self):
        pass
    
    '''
    '''
    def export_fire_location(self):
        pass
