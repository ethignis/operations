from image_overlaying import *
from common.thermal_subscriber import ThermalCameraSubscriber
from common.visual_subscriber import VisualSubscriber
import rospy 
import cv2

def main():
    rospy.init_node("Test",anonymous=True)
    thermal = ThermalCameraSubscriber()
    visual = VisualSubscriber()
    while True:
        thermal_img = thermal.get_thermal_image()
        visual_img = visual.get_visual_image()
        img = overlay_image(thermal_img, visual_img)
        cv2.imshow("test",cv2.resize(img,(800,600)))
        #cv2.imshow("test",cv2.resize(visual_img,(800,600)))
        cv2.waitKey(10)

if __name__ == "__main__":
    main()