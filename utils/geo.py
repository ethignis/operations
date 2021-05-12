import pyproj
import geocoder
import numpy as np
'''
@function:
@param:
@output: 
@TODO: need to set up the mavlink connection for getting the 
        GPS location
'''
def get_GPS():
    pass

'''
@function: get the elevation of the location based on its GPS position
@param: lat - latitude
        long - longitude
@output: the elevation at the position
@TODO: this method requires Google API.
'''
def get_elevation(lat,lng):
    g = geocoder.google([lat,lng], method="elevation")
    return g.meters
