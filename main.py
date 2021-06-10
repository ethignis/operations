'''
This is the main class which runs everything.
@TODO: Multithreading subscription
       3 Threads essentially -> 1 for merging MAVROS and Image
                                1 for merging visual and thermal
                                1 for thermal
'''
from common.temperature import get_temp
from common.thermal_subscriber import ThermalCameraSubscriber
import cv2
import rospy
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image

def publish_fire_detection(img):
   pub_text = rospy.Publisher('fire_detection/text', String, queue_size=10)
   pub_img = rospy.Publisher('fire_detection/img', Image, queue_size=10)
   rate = rospy.Rate(10) # 10hz
   
def main():
   rospy.init_node("main",anonymous=True)


if __name__ == "__main__":
   main()