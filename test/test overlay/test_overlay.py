
import sys
sys.path.append('../../operations')
from image_overlaying import ImageOverlay

import cv2 as cv

img_thermal = cv.imread('1-0.jpg')
img_visual = cv.imread('1-1.jpg')

img_overlayed = ImageOverlay.overlay_image(img_thermal,img_visual)

cv.imwrite("overlayed.jpg", img_overlayed)