import pyproj
import geocoder
import numpy as np

class FireLocalizer:
    def __init__(self):
        self.K = None
        self.R = None
        self.t = None
        self.relative = None
    '''
