import cv2
 
img = cv2.imread('/home/ignis/workspace/camera/mounted_images/9-0.jpg', cv2.IMREAD_UNCHANGED)
 
print('Original Dimensions : ',img.shape)
 
width = 4000  
height = 3000
dim = (width, height)
 
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
 
print('Resized Dimensions : ',resized.shape)

cv2.imwrite('/home/ignis/workspace/camera/mounted_images/9-0-resized.jpg', resized) 
# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()