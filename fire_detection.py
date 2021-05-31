'''
This is used to detect the fire in the sceneary. It does not however
tell where the fire is. That could be certainly be implemented with the
thermal camera. I would implement 
'''

'''
@function: detect whether there exists fires in the sceneary. Thermal
           approach uses thresholding by tracking whether there is a 
           particular hot pixel. Visual approach would rely on using
           machine learning classification approach
@param: img - input image
@output: true if there is fire; false otherwise
'''

from common.temperature import *
import numpy as np

'''
@function: detect the location of fire
@thermal:
'''
def detect_fire_thermal():
    FIRE_TEMP = 50
    img = get_temp()
    if img[img >FIRE_TEMP].shape[0] > 0:
        return True
    else:
        return False 

def detect_fire_visual(img):
    pass

'''
@function: mark fire pixels in the image
@param: img - input image
@output: a masking for segmentation of fire/non-fire region
'''
def track_fire_thermal(gps=True):
    FIRE_TEMP = 50
    img = get_temp()
    mask = img > FIRE_TEMP
    # if gps:
    #     store_img(i
    return mask

def track_fire_visual(img):
    pass

def detect_and_track_fire_thermal():
    FIRE_TEMP = 50
    img = get_temp()