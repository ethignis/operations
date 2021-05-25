import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

def callback_temp(img):
   bridge = CvBridge()
   return bridge.imgmsg_to_cv2(img)

def get_temp():
   topic = "/thermalgrabber_ros/image_deg_celsius"
   rospy.init("Temperature",anonymous=True)
   raw_to_kelvin_factor = 0.04
   kKelvinToCelsiusShift = -273.15

   temp_map = callback_temp(rospy.wait_for_message(topic,Image))
   temp_map = raw_to_kelvin_factor *temp_map + kKelvinToCelsiusShift
    