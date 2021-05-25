class ImageOverlay:
    def __init__(self):
        pass
    
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

for i in range(1,11):

    img = cv.imread('../mounted_images/{}-0.jpg'.format(i))

    rows,cols,ch = img.shape
    pts1 = np.float32([[170,163],[375,190],[205,290],[329,329]])
    pts2 = np.float32([[420,500],[2550,850],[700,1850],[1900,2350]])
    M = cv.getPerspectiveTransform(pts1,pts2)
    img = cv.warpPerspective(img,M,(4000,3000))

    # "Almost black" color range
    lower = np.array ([0,0,0])
    upper = np.array ([40,40,40])
    #Create mask
    img_mask = cv.inRange (img, lower, upper) # Extraction mask for "almost white" only
    img_mask = cv.bitwise_not (img_mask, img_mask) # Inversion = Extraction mask other than "almost white"
    # Extract all except "almost vlack" → make "almost black" transparent
    img = cv.bitwise_and (img, img, mask = img_mask)

    img2 = cv.imread ('../mounted_images/{}-1.jpg'.format(i), cv.IMREAD_COLOR)

    # cv.imwrite("overlay-{}.jpg".format(i), img)
    dst = cv.addWeighted(img,1,img2,1,0)

    cv.imwrite("overlay-{}.jpg".format(i), dst)
