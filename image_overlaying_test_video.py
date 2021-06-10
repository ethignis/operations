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
    print("ros initialized")
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


    #for saving to video
    img_array = []
    thermal_img_array = []
    visual_img_array = []
    size = (4000,3000)
    
    out1 = cv2.VideoWriter('thermal.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
    out2 = cv2.VideoWriter('visual.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
    out3 = cv2.VideoWriter('overlayed.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

    #overlay the images
    try:
        while True:
            # read data
            print("thermal")
            thermal_img = thermal.get_thermal_image()
            print("visual")
            visual_img = visual.get_visual_image()
            print("visual append")
            visual_img_array.append(visual_img)
            print("thermal append")
            thermal_img_array.append(thermal_img)
            
                

    except KeyboardInterrupt:
            print("Press Ctrl-C to terminate while statement")
            pass    

    #put data in video
    print("start writing data")
    print(len(thermal_img_array))
    print(len(visual_img_array))
    for i in range(len(thermal_img_array)):
        out1.write(thermal_img_array[i])
        out2.write(visual_img_array[i])
        out3.write(overlay_image(thermal_img_array[i], visual_img_array[i]))
    out1.release()
    out2.release()
    out3.release()

if __name__ == "__main__":
    main()