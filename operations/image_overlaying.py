import numpy as np
import cv2
import matplotlib.pyplot as plt

class ImageOverlay:
    def __init__(self):
        pass
    
    def overlay_image(img1,img2):
        pass
    
# Piepeline:
# Upsampling -> Scaling ->Shifting
#for i in range(1,11):
def overlay_img(thermal_img,visual_img):
    #img = cv.imread('../mounted_images/{}-0.jpg'.format(i))
    # Upsample the image
    
    # Shape of the object
    rows,cols,ch = thermal_img.shape
    pts1 = np.float32([[170,163],[375,190],[205,290],[329,329]])
    pts2 = np.float32([[420,500],[2550,850],[700,1850],[1900,2350]])
    M = cv2.getPerspectiveTransform(pts1,pts2)
    thermal_img = cv2.warpPerspective(thermal_img,M,(4000,3000))

    # "Almost black" color range
    lower = np.array ([0,0,0])
    upper = np.array ([40,40,40])
    #Create mask
    img_mask = cv2.inRange(thermal_img, lower, upper) # Extraction mask for "almost white" only
    img_mask = cv2.bitwise_not (img_mask, img_mask) # Inversion = Extraction mask other than "almost white"
    # Extract all except "almost vlack" → make "almost black" transparent
    img = cv2.bitwise_and(thermal_img, thermal_img, mask = img_mask)

    img2 = visual_img #cv2.imread('../mounted_images/{}-1.jpg'.format(i), cv.IMREAD_COLOR)

    # cv.imwrite("overlay-{}.jpg".format(i), img)
    dst = cv2.addWeighted(img,1,img2,1,0)

    return dst
