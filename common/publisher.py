#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image

def image_talker(img,name="Talker"):
    pub = rospy.Publisher(name,Image,queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
  