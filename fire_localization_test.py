import numpy as np
import data.vtol
#from common.metadata import MetaData
import common.coordinate
from fire_detection import *
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from common.geojson import export_geojson

def main():
    rospy.init_node("Fire localization", anonymous=True)
    bridge = CvBridge()

    init_gps = get_gps()
    fire_localizer = FireLocalizer(init_gps)
    topic = "fire_detection/img"
    count = 0
    #pub_text = rospy.Publisher('fire_localization/text', String, queue_size=10)
    #pub_gps = rospy.Publisher('fire_detection/img', Image, queue_size=10)
    while True:
        # Check the mask from the fire detection to see if there exists a particular pixel for 
        # fire detection -> based on each pixel, we operate the fire localization
        mask = rospy.wait_for_message(topic,Image)
        mask = bridge.imgmsg_to_cv2(mask)
        fire_localizer.localize_fire_thermal(mask)
        ps = fire_localizer.export_fire_location()
        if ps:
            export_geojson(ps)
            count += 1


if __name__ == "__main__":
    main()