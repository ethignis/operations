from nav_msgs.msg import Odometry
from sensor_msgs.msg import NavSatFix
from scipy.spatial.transform import Rotation as R
import rospy
import numpy as np
#from point import Point

# rospy.init_node("mavros",anonymous=True)

'''
@function: callback function to extract the linear and angular position and velocity
@param: odom_data - odometry message
@return: lin_pos - linear position
         ang_pos - angular position
         lin_vel - linear velocity
         ang_vel - angular velocity
'''
def callback_odm(odom_data):
  lin_pos = odom_data.pose.pose.position
  lin_pos = np.array([lin_pos.x,lin_pos.y,lin_pos.z])
  ang_pos = odom_data.pose.pose.orientation
  ang_pos = np.array([ang_pos.x,ang_pos.y,ang_pos.z, ang_pos.w])
  lin_vel = odom_data.twist.twist.linear
  lin_vel = np.array([lin_vel.x,lin_vel.y,lin_vel.z])
  ang_vel = odom_data.twist.twist.angular
  ang_vel = np.array([ang_vel.x,ang_vel.y,ang_vel.z])
  return lin_pos, ang_pos, lin_vel, ang_vel

'''
@function: a callback function to return the triple tuple of latitute, longitude and altitude
@param: gps_data - GPS data in ros message
@return: an array of latitude, longitude and altitude
'''
def callback_gps(gps_data):
  lat = gps_data.latitude
  lng = gps_data.longitude
  alt = gps_data.altitude
  return np.array([lat, lng, alt])

def get_odometry():
  topic = "/mavros_node/local_position/odom"
  #rospy.init_node("odom",anonymous=True)
  lin_pos, ang_pos, lin_vel, ang_vel = callback_odm(rospy.wait_for_message(topic,Odometry))
  #rospy.Subscriber(topic,Odometry,callback_odm)
  return lin_pos, quat2rot(ang_pos), lin_vel, ang_vel
  #print("{} {} {} {}".format(lin_pos, ang_pos, lin_vel, ang_vel))
# Odometry -> PoseWithCov -> Pose -> Position and Orienttaion

def get_gps():
  topic = "/mavros_node/global_position/raw/fix"
  #rospy.init_node("gps",anonymous=True)
  #rospy.Subscriber(topic, NavSatFix, callback_gps)
  gps = callback_gps(rospy.wait_for_message(topic,NavSatFix))
  return gps

def quat2rot(quat):
  r = R.from_quat(quat.tolist())
  return r.as_dcm()#r.as_matrix()


# def main():
#   get_odometry()

# if __name__ == "__main__":
#     main()
