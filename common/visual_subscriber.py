import cv2
import rospy
import importlib
import unittest
from sensor_msgs.msg import Image
from web import fetch_visual_data
from cv_bridge import CvBridge

class VisualSubscriber:
    def __init__(self, save=False):
        self.running_subscribers = []
        self.visual_topic = ["/camera/image_color",
                        "/camera/image_mono",
                        "/camera/image_raw"]

        rospy.init_node("visual_camera",anonymous=True)
        self.save = save
        self.j = 0

    def img2cv2(self,img):
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(img, "bgr8")
        return cv_image        

    '''
        Function: callback
        Description: a dummy callback function as a placeholder
        Input: data - data returned by ROS node
        Output: none
    '''
    def callback(data):
        print(data.data)

    '''
        Function: subscribe
        Description: subscribe to a specific topic
        Input: topic - the topic to which the subscriber subscribers
               callback - the function called once data is fetechd
        
        Output: none
    '''
    # def subscribe(self,topic,callback=self.callback):
    #     if unittest.assertNotIn(topic,self.nodes.keys()):
    #         raise Exception("{} is not in the topic list!".format(topic))
    #     module_name = self.nodes[topic]
    #     importlib.import_module(module_name[0],module_name[1])
    #     rospy.Subscriber(topic,module_name[1],callback)
    #     self.running_subscribers.append([topic,module_name[1]])
    
    '''
        Function: listen
        Input: subscriber - a list structure of [topic_name, return_data]
               all - a flag for whether returning data for all running nodes
        
        Output: a dictionary with topic name as the key and data as value
    '''
    def listen(self):
        while not rospy.is_shutdown():
            data = []
            self.running_subscribers = fetch_visual_data()
            self.j += 1
            for i,subscriber in enumerate(self.running_subscribers):
                data.append(rospy.wait_for_message(subscriber,Image))
                if self.save==True:
                    filename = "./visual_images/{}-{}.jpg".format(subscriber,self.j)
                    cv2.imwrite("./visual_images/"+str(i)+"-"+str(self.j)+".jpg",self.img2cv2(data[i]))
                    print('saved {}'.format(self.j))
                cv2.imshow(subscriber,self.img2cv2(data[i]))
                cv2.waitKey(2000)
 
        rospy.spin()