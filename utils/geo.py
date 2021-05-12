import pyproj
import geocoder
import numpy as np
'''
@function:
@param:
@output: 
@TODO: need to set up the mavlink connection for getting the 
        GPS location
'''
def get_GPS(self):
    pass

'''
@function:
@param:
@output:
@TODO:
'''
def get_projection(self):
    pass

'''
@function: get the elevation of the location based on its GPS position
@param: lat - latitude
        long - longitude
@output: the elevation at the position
@TODO: this method requires Google API. It would be better to make it work with 
'''
def get_elevation(self,lat,lng):
    g = geocoder.google([lat,lng], method="elevation")
    return g.meters

'''
@function: convert the world coordinate into the world coorinate
@param: 
@output:
'''
def world2cam(self, R, t):
    pass 

'''
@function:
@param:
@output: 
'''
def cam2image(self):
    pass

def adjust_image(self):
    pass

def 
'''
@function: convert the normal coordinate into the homogeneous coordinate
@param: p - the coordinate in the inhomogeneous coordinate
        n - the dimension of the original coordinate
@output: the corresponding homogeneous coordinate
'''
def cor2hom(self, p, n):
    assert p.shape[0] == n, "The coordinate is already in the homogeneous coordinate!"
    return np.Concatenate((p,1),axis=None)

'''
@function: convert the homogeneous coordinate into the original coordiante
@param: p - the coordinate in the homogeneous coordinate
        n - the dimension of the original coordinate
@output: the corresponding inhomogeneous coordinate 
'''
def hom2cor(self, p, n):
    assert p.shape[0] == n+1, "The coordinate is not in the homogeneous coordiante!"
    assert p[-1] != 0, "The point is at the infinity!"
    for i in range(n-1):
        p[i] = p[i] / p[-1]
    return p