'''
This is used to overlay the interesting parts of the thermal image
to the visual image 
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

# class ImageOverlay:
#     def __init__(self):
#         pass
    
'''
@function: overlays two images
@param: img_thermal image from the thermal camera
@param: img_visual image from the visual camera
@output: the overlayed image of both cameras
'''
def overlay_image(img_thermal,img_visual):
    #set parameters for transforming the thermal image
    pts1 = np.float32([[170,163],[375,190],[205,290],[329,329]])
    pts2 = np.float32([[420,500],[2550,850],[700,1850],[1900,2350]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    #transform the thermal image to the new size and perspective
    img_thermal = cv2.warpPerspective(img_thermal,M,(2000,1500))#(4000,3000))#
    img_thermal = cv2.cvtColor(img_thermal,cv2.COLOR_GRAY2RGB)
    #set parameters to remove the almost black (cold) areas in the thermal image
    lower = np.array ([0,0,0])
    upper = np.array ([40,40,40])
    #create mask for filtering the image
    print(img_thermal.shape)
    print(img_visual.shape)
    img_mask = cv2.inRange (img_thermal, lower, upper) # Extraction mask for "almost white" only
    img_mask = cv2.bitwise_not (img_mask, img_mask) # Inversion = Extraction mask other than "almost white"
    #extract all except "almost black" pixels, this makes "almost black" transparent
    img_thermal_filtered = cv2.bitwise_and (img_thermal, img_thermal)#, mask = img_mask)
    
    #overlay the two images
    img_overlayed = cv2.addWeighted(img_thermal_filtered,1,img_visual,1,0)

    return img_overlayed

