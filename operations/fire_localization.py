import pyproj
import geocoder
import numpy as np
import utils.vtol
import utils.coordinate
from utils.start_flight import MetaData
class FireLocalizer:
    def __init__(self):
        '''
        '''
        self.init = MetaData()
        self.p = []

    def localize_fire(self):
        img = self.get_image()
        if detect_file(img) == True:

    def get_image(self):
        pass
    '''
    '''
    def export_fire_location(self):
        pass
