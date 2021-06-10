from image_overlaying import *
from common.thermal_subscriber import ThermalCameraSubscriber
from common.visual_subscriber import VisualSubscriber
import rospy 
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def main():

    #initialization of the cameras and node
    print("start of programm")
    bridge = CvBridge()
    rospy.init_node("overlay_image",anonymous=True)
    pub = rospy.Publisher('overlay_image/img', Image, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    print("publisher released")
    thermal = ThermalCameraSubscriber()
    print("thermal released")
    visual = VisualSubscriber()
    print("visual released")

    #to take only one picture from the actual situation set safe = True
    save=False
    if save == True:
        print("start saving")
        thermal_img = thermal.get_thermal_image()
        print("thermal is fine")
        visual_img = visual.get_visual_image()
        print("visual is fine")
        shot = "test"   
        cv2.imwrite("data/mounted_images/thermal-{}.jpg".format(shot), thermal_img)
        cv2.imwrite("data/mounted_images/visual-{}.jpg".format(shot), visual_img)
        return


  

    #overlay the images
    while True:
        # read data
        thermal_img = thermal.get_thermal_image()
        visual_img = visual.get_visual_image()
        # overlay
        img = overlay_image(thermal_img, visual_img)


        
            #publis to rostopic
        #pub.publish(bridge.cv2_to_imgmsg(img))
        #rate.sleep()
        
            #for displaying
        cv2.imshow("overlayed",cv2.resize(img,(800,600)))
        cv2.imshow("thermal",cv2.resize(thermal_img,(800,600)))
        cv2.imshow("visual",cv2.resize(visual_img,(800,600)))
        cv2.waitKey(10)



if __name__ == "__main__":
    main()