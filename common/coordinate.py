import numpy as np
import sys
from pyproj import Transformer, CRS

'''
@functions: rotation matrices
@param: angle given in degree
@output: corresponding rotation matrices
'''
def roll(angle):
    angle = np.radians(angle)
    return np.array([[np.cos(angle),-np.sin(angle),0],[np.sin(angle),np.cos(angle),0],[0,0,1]])

def yaw(angle):
    angle = np.radians(angle)
    return np.array([[1,0,0],[0,np.cos(angle),-np.sin(angle)],[0,np.sin(angle),np.cos(angle)]])

def pitch(angle):
    angle = np.radians(angle)
    return np.array([[np.cos(angle),0,np.sin(angle)],[0,1,0],[-np.sin(angle),0,np.cos(angle)]])

'''
@function: convert the GPS location into the flat rectangular grid 
           by using the projection from WGS86 to LV03 -> ONLY SUITABLE FOR SWITZERLAND!
@param: lat - latitude
        lng - longitude
@output: the projected location of the object in LV03 Eucledian coordinate
'''
def gps2world(lat,lng):
    # 4326 is the identifier for WGS 86
    crs_4326 = CRS.from_epsg(4326) 
    # 21781 is the identifier for LV03/CH1903
    crs_21781 = CRS.from_epsg(21781)
    transformer_4326_2_21781 = Transformer.from_crs(crs_4326,crs_21781)
    pos = transformer_4326_2_21781.transform(lat,lng)
    return np.array(pos)

'''
@function: convert the into the flat rectangular grid GPS location
           by using the projection from LV03 to WGS86 -> ONLY SUITABLE FOR SWITZERLAND!
@param: x - x-axis
        y - y-axis
@output: the projected location of the object in gps coordinate
'''
def world2gps(x,y):
    # 4326 is the identifier for WGS 86
    crs_4326 = CRS.from_epsg(4326) 
    # 21781 is the identifier for LV03/CH1903
    crs_21781 = CRS.from_epsg(21781)
    transformer_21781_2_4326 = Transformer.from_crs(crs_21781,crs_4326)
    gps = transformer_21781_2_4326.transform(x,y)
    return np.array(gps)

'''
@function: convert the world coordinate into the body coordinate
@param: R - the rotation matrix from world to body
        t - the translation vector world to body
        x_in - the input vector in the inhomogeneous coordinate
        n - the dimension of the input vector
@output: the object in the body coordinate
@TODO: ADD R AND T AS DEFAULT VALUE
'''
def world2body(R, t, x_in, n):

    return affine_transform(R,t,x_in,n)

def body2world(R, t, x_in, n):
    return affine_inverse(R,t,x_in,n)

'''
@function: convert from the body coordinate
           to the camera coordinate (the location of PX4)
@param: R - the rotation matrix from body to cam
        t - translation matrix from body to cam
@output: the location in the camera coordinate
@comment: the unit is in mm, it is in the typical body coordinate for the plane
@TODO: ADD R AND T AS DEFAULT VALUE
'''
def body2thermal_cam(x_in, n):
    R = np.dot(yaw(90),pitch(50))
    t = np.array([[377.7033],[-40],[109.4655]])
    return affine_transform(R,t,x_in,n)

def body2visual_cam(x_in, n):
    R = np.dot(yaw(90),pitch(50))
    t = np.array([[377.7033],[40],[109.4655]])
    return affine_transform(R,t,x_in,n)

'''
@function: convert from the camera coordinate
           to the body coordinate (the location of PX4)
@param: R - the rotation matrix from body to cam
        t - translation matrix from body to cam
@output: the location in the body coordinate
@TODO: ADD R AND T AS DEFAULT VALUE
'''
def thermal_cam2body(x_in, n):
    R = np.dot(yaw(90),pitch(50))
    t = np.array([[377.7033],[-40],[109.4655]])
    return affine_inverse(R,t,x_in,n)

def visual_cam2body(x_in, n):
    R = np.dot(yaw(90),pitch(50))
    t = np.array([[377.7033],[40],[109.4655]])
    return affine_inverse(R,t,x_in,n)

'''
@function: convert the camera coordinate into the image coordinate
@param: K - intrinsic matrix
        x_in - inhomogeneous coordinate
        n - the dimension of the vector        
@output: inhomogenous coordinate
@TODO: ADD K AS DEFAULT VALUE
'''
def cam2img(K,x_in, n):
    x = inhom2hom(x_in,n)
    y = np.dot(K,x)
    return hom2inhom(y,n)

'''
@function: convert the image coordinate into the camera coordinate
@param: K - intrinsic matrix
        x_in - inhomogeneous coordinate
        n - the dimension of the vector
@output: inhomogenous camera coordinate
@TODO: ADD K AS DEFAULT VALUE
'''
def img2cam(K,x_in, n):
    x = inhom2hom(x_in,n)
    y = np.dot(np.linalg.inv(K),x)
    return hom2inhom(y,n)

'''
@function: convert the normal coordinate into the homogeneous coordinate
@param: p - the coordinate in the inhomogeneous coordinate
        n - the dimension of the original coordinate
@output: the corresponding homogeneous coordinate
'''
def inhom2hom(p, n):
    assert p.shape[0] == n, "The coordinate is already in the homogeneous coordinate!"
    return np.concatenate((p,1),axis=None)

'''
@function: convert the homogeneous coordinate into the original coordiante
@param: p - the coordinate in the homogeneous coordinate
        n - the dimension of the original coordinate
@output: the corresponding inhomogeneous coordinate 
'''
def hom2inhom(p, n):
    assert p.shape[0] == n+1, "The coordinate is not in the homogeneous coordiante!"
    assert p[-1] != 0, "The point is at the infinity!"
    for i in range(n-1):
        p[i] = p[i] / p[-1]
    return p

'''
# @function: check the homogeneity of the vector and convert to the homogeneous coordinate if needed
# @param: x_in - inhomogeneous coordinate
#         x_hom - homogeneous coordinate
# @output: homogeneous coordinate
# '''
# def check_hom(x_in=None,x_hom=None):
#     if x_in == None and x_hom == None:
#         sys.exit("At least either homogeneous or inhomogeneous coordinate must be given!")
#     if x_in != None:
#         x = inhom2hom(x_in)
#     else:
#         x = x_hom
#     return x 

'''
@function: convert the affine transformation into the homogeneous matrix form
@param: R - rotation matrix
        t - trasnlation vector
        n - dimension of the vector
@output: a homogeneous affine transformation matrix in homogeneous coordinate
'''
def affine2matrix(R,t,n):
    assert R.shape[1] == n, "The dimension of the rotation matrix does not match!"
    assert t.shape[0] == n, "The dimension of the translation vector does not match!"
    T1 = np.concatenate((R,np.zeros([1,3])))
    T2 = inhom2hom(t,n).reshape([n+1,1])
    return np.concatenate((T1,T2),axis=1)

'''
@function: perform forward affine transform
@param: R - the rotation matrix
        t - the translation vector
        x_in - the inhomogeneous vector
        n - the dimension of the vector
@output: the output transformed vector in inhomogeneous coordinate
'''
def affine_transform(R,t,x_in,n):
    assert R.shape[1] == n, "The dimension of the rotation matrix does not match!"
    assert t.shape[0] == n, "The dimension of the translation vector does not match!"
    assert x_in.shape[0] == n, "The dimension of the input is in homogeneous coordinate!"
    x_hom = inhom2hom(x_in,n)
    return hom2inhom(np.dot(affine2matrix(R,t,n),x_hom),n)

def affine_inverse(R,t,x_in,n):
    return affine_transform(R.t, -t, x_in,n)

'''
@function: find the intersection between a line and a plane
@param: p - the point on the line
        line - the vector direction of the line
        plane - the parametric representation of the plane
@output: the point of intersection
'''
def get_line_plane_intersection(p, line, plane):
   pass 