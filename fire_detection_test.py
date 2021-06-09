from common.temperature import get_temp
from common.thermal_subscriber import ThermalCameraSubscriber
import cv2
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
   rospy.init_node("test",anonymous=True)
   bridge = CvBridge()
   # Publisher of the fire text
   pub_text = rospy.Publisher('fire_detection/text', String, queue_size=10)
   # Publisher of the fire image
   pub_img = rospy.Publisher('fire_detection/img', Image, queue_size=10)
   # Publisher of the segmented fire image
   pub_seg = rospy.Publisher('fire_segmentation/img', Image, queue_size = 10)
   rate = rospy.Rate(10) # 10hz
   text = "There is no fire"
   while not rospy.is_shutdown():
      a = get_temp()
      b = ThermalCameraSubscriber()
      b_img = b.get_thermal_image()
      #a = a.astype(int)
      FIRE_TEMP = 50
      print(a.shape)
      mask = np.array(a>FIRE_TEMP).astype(float)#.astype(int)
       #print(cv2.bitwise_and(b_img,b_img,mask = mask.astype(int)))
      count = 0
      if a[a>FIRE_TEMP].shape[0] > 0:
         if count == 4:
            print("There is fire")
            print(a)
            text = "There is fire"
         else:
            count += 1
      else:
         print("No fire")
         print(a)
         text = "There is no fire"
         count = 0
      #cv2.imshow("test",mask)#cv2.bitwise_and(b,mask))
      #cv2.waitKey(10)
      # img_seg = 
      pub_text.publish(text)
      pub_img.publish(bridge.cv2_to_imgmsg(mask))
      pub_seg.publish(bridge.cv2_to_imgmsg(img_seg))
      rate.sleep()
    
if __name__ == "__main__":
   main()
