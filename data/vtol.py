import pyproj
import geocoder
import numpy as np
'''
@function:
@param:
@output: [lat, lng, alt] of the current location
@TODO: need to set up the mavlink connection for getting the 
        GPS location
       THIS WOULD BE IMPLEMENTED IN ROS
'''
def get_current_location():
    pass

'''
@function: retrieve the (yaw, pitch, roll) of the airplane
@param: 
@output: the angle
@TODO: MAVLINK
'''
def get_angle():
    pass

'''
@function: retrieve the flying direction w.t.t north and east
@param: 
@output: the direction
@TODO: MAVLINK
'''
def get_direction():
    pass

'''
@function: retrieve the height over the ground
@param: none
@output: the height of the current drone over the ground
@TODO: adapt it such that we are not just using the initial elevation as the relative zero point
'''

# def get_height():
#     curr_elev = get_GPS()
#     height = curr_elev - init_elev
#     return height

