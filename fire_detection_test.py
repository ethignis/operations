from common.temperature import get_temp
from common.thermal_subscriber import ThermalCameraSubscriber
import cv2
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image


def main():
   rospy.init_node("test",anonymous=True)
   pub_text = rospy.Publisher('fire_detection/text', String, queue_size=10)
   pub_img = rospy.Publisher('fire_detection/img', Image, queue_size=10)
   rate = rospy.Rate(10) # 10hz

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
            print("there is fire")
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
      #pub.publish(text)
      rate.sleep()
    
if __name__ == "__main__":
   main()
