from typing_extensions import Concatenate
import numpy as np

'''
@function: convert the GPS location into the flat rectangular grid 
@param: lat - latitude
        lng - longitude
@output:
'''
def gps2world(lat,lng):
    pass
'''
@function: convert the world coordinate into the world coorinate
@param: 
@output:
'''
def world2cam(R, t):
    pass 

'''
@function:
@param:
@output: 
'''
def cam2image():
    pass

def adjust_image():
    pass

'''
@function: convert the normal coordinate into the homogeneous coordinate
@param: p - the coordinate in the inhomogeneous coordinate
        n - the dimension of the original coordinate
@output: the corresponding homogeneous coordinate
'''
def cor2hom(p, n):
    assert p.shape[0] == n, "The coordinate is already in the homogeneous coordinate!"
    return np.concatenate((p,1),axis=None)

'''
@function: convert the homogeneous coordinate into the original coordiante
@param: p - the coordinate in the homogeneous coordinate
        n - the dimension of the original coordinate
@output: the corresponding inhomogeneous coordinate 
'''
def hom2cor(p, n):
    assert p.shape[0] == n+1, "The coordinate is not in the homogeneous coordiante!"
    assert p[-1] != 0, "The point is at the infinity!"
    for i in range(n-1):
        p[i] = p[i] / p[-1]
    return p

'''
@function: convert the affine transformation into the homogeneous matrix form
@param: R - rotation matrix
        t - trasnlation vector
        n - dimension of the vector
@output: a homogeneous affine transformation matrix in homogeneous coordinate
'''
def affine2matrix(R,t,n):
    T1 = np.concatenate((R,np.zeros([1,3]))
    T2 = cor2hom(t,n).reshape([n+1,1])
    return np.concatenate((T1,T2),axis=1)