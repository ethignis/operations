'''
A test function to mark the path/trajectory of the drone
'''

from common.mavros import get_gps
from common.point import Point, export_point
from sensor_msgs.msg import NavSatFix
from nav_msgs.msg import Odometry
import rospy

def main():
    rospy.init_node("path",anonymous=True)
    count = 0 
    while True:
        gps = get_gps()
        
        