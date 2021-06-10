'''
A main test function to collect data
'''

import rospy
from common.mavros import g
def main():
    rospy.init_node("Collect",anonymous=True)
    
if __name__ == "__main__":
    main()
    