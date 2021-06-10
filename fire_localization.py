'''
This operation is used to localize the location of the fire such that 
fires could be marked on the map
'''

import numpy as np
import data.vtol
from common.metadata import MetaData
#from common.point import Point
import common.coordinate
from fire_detection import *

class FireLocalizer:
    def __init__(self,init_gps):
        '''
        '''
        self.init = MetaData(init_gps)
        self.p = []
    
    '''
    @function: localize the location of the fire based on the thermal camera image
    @param: mask - mask image of where data are
    @output: the GPS location of each corresponding fire pixel in the mask
    '''
    def localize_fire_thermal(self,mask):
        #mask =  track_fire_thermal()
        # index list of fire px
        pxes = np.where(mask)
        if pxes[0].size > 0:
            for i in range(pxes[0].shape):
                #@TODO: Check if the order is correct
                px_img = np.array([pxes[0][i],pxes[1][i]])
                px_thermal_cam = img2thermal_cam(px_img)
                px_body = thermal_cam2body(px_thermal_cam)
                px_world = body2world(px_body)
                n = np.array([0,0,self.init.init_gps])
                p =  body2world(thermal_cam2body(np.array([0,0,0])))
                pt = get_line_plane_intersection(p,px_world,n)
                # TODO: Implement the flag in the coordinate
                #pt = Point(pt_cam,"thermal_cam2gps")
                self.p.append(world2gps(pt))

    # def localize_fire_visual(self):
    #     img = self.get_image()
    #     mask = track_fire_visual()
    #     # index list of fire px
    #     pxes = np.where(mask)
    #     for px in pxes:
    #         col = px[0]
    #         row = 
    #         p1 = Point(px,"visual2gps")
    #         pt_cam = common.coordinate.get_line_plane_intersection(p1.visual,self.init.init_pt.visual)
    #         # TODO: Implement the flag in the coordinate
    #         pt = Point(pt_cam,"visual_cam2gps")
    #         self.p.append(pt.gps)

    '''
    '''
    def export_fire_location(self):
        return self.p

    