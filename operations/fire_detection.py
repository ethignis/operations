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

def detect_fire_thermal(img):
    pass

def detect_fire_visual(img):
    pass

'''
@function: mark fire pixels in the image
@param: img - input image
@output: a masking for segmentation of fire/non-fire region
'''
def track_fire_thermal(img):
    pass

def track_fire_visual(img):
    pass