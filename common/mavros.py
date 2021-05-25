from nav_msgs.msg import Odometry
from scipy.spatial.transform import Rotation as R


def get_direction():
  return 1

def get_odometry():
  pass

# Odometry -> PoseWithCov -> Pose -> Position and Orienttaion

def quat2rot(quat):
    r= R.from_quat(quat)
    return r.as_matrix()
