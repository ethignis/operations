
import cv2
import rospy
import importlib
import unittest
from sensor_msgs.msg import Image
from web import fetch_data
from cv_bridge import CvBridge

'''
    Class: ThermalCameraSubscriber
    Description: the class takes consideration of all 
                 possible outputs possible from thermal camera
                 grabbers and stream 
'''
class ThermalCameraSubscriber:
    def __init__(self,save=False):
        self.running_subscribers = []
        self.thermal_topic = ["/thermalgrabber_ros/image_mono8",
                        "/thermalgrabber_ros/image_mono16",
                        "/thermalgrabber_ros/image_deg_celsius",
                        "/thermalgrabber_ros/image_color"]

        rospy.init_node("thermalgrabber_ros",anonymous=True)
        self.save = save
        self.j = 0

    '''
        Function: callback
        Description: a dummy callback function as a placeholder
        Input: data - data returned by ROS node
        Output: none
    '''
    def callback(data):
        print(data.data)

    def get_mono8(self):
        return rospy.wait_for_message(self.thermal_topic[0],Image)

    def get_mono16(self):
        return rospy.wait_for_message(self.thermal_topic[1],Image)

    def get_image_celsius(self):
        return rospy.wait_for_message(self.thermal_topic[2],Image)

    def get_image_color(self):
        return rospy.wait_for_message(self.thermal_topic[3],Image)

    def img2cv2(self,img):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(img)
        return cv_image
    '''
        Function: listen
        Input: subscriber - a list structure of [topic_name, return_data]
               all - a flag for whether returning data for all running nodes
        
        Output: a dictionary with topic name as the key and data as value
    '''
    def listen(self):
        while not rospy.is_shutdown():
            data = []
            self.running_subscribers = fetch_data()
            self.j += 1
            for i,subscriber in enumerate(self.running_subscribers):
                data.append(rospy.wait_for_message(subscriber,Image))
                #print(data)
                if self.save==True:
                    filename = "./images1/{}-{}.jpg".format(subscriber,self.j)
                    cv2.imwrite("./images1/"+str(i)+"-"+str(self.j)+".jpg",self.img2cv2(data[i]))
                    print('saved')
                cv2.imshow(subscriber,self.img2cv2(data[i]))
                cv2.waitKey(10)
 
        rospy.spin()