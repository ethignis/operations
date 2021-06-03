from image_overlaying import *
from common.thermal_subscriber import ThermalCameraSubscriber
from common.visual_subscriber import VisualSubscriber
import rospy 
import cv2

def main():
    print("start of programm")
    rospy.init_node("Test",anonymous=True)
    thermal = ThermalCameraSubscriber()
    print("thermal released")
    visual = VisualSubscriber()
    print("visual released")

    save=False
    if save == True:
        print("start saving")
        thermal_img = thermal.get_thermal_image()
        print("thermal is fine")
        visual_img = visual.get_visual_image()
        print("visual is fine")
        shot = 7   
        cv2.imwrite("data/mounted_images/thermal-{}.jpg".format(shot), thermal_img)
        cv2.imwrite("data/mounted_images/visual-{}.jpg".format(shot), visual_img)
        return
    while True:
        thermal_img = thermal.get_thermal_image()
        visual_img = visual.get_visual_image()
        img = overlay_image(thermal_img, visual_img)
        cv2.imshow("test",cv2.resize(img,(800,600)))
        #cv2.imshow("test",cv2.resize(visual_img,(800,600)))
        cv2.waitKey(10)

if __name__ == "__main__":
    main()