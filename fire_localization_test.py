import numpy as np
import data.vtol
#from common.metadata import MetaData
import common.coordinate
from fire_detection import *

def main():
    rospy.init_node("Fire localization", anonymous=True)
    init_gps = get_gps()
    fire_localizer = FireLocalizer()

if __name