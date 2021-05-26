'''
This operation is used to localize the location of the fire such that 
fires could be marked on the map
'''

import numpy as np
import data.vtol
from common.metadata import MetaData
from common.point import Point
import common.coordinate
from operations.fire_detection import *

class FireLocalizer:
    def __init__(self):
        '''
        '''
        self.init = MetaData()
        self.p = []

    def localize_fire_thermal(self):
        img = self.get_image()
        mask =  track_fire_thermal()
        for px in pxes:
            p1 = Point(px,"thermal2gps")
            pt_cam = common.coordinate.get_line_plane_intersection(p1.thermal,self.init.init_pt.thermal)
            # TODO: Implement the flag in the coordinate
            pt = Point(pt_cam,"thermal_cam2gps")
            self.p.append(pt.gps)

    def localize_fire_visual(self):
        img = self.get_image()
        if detect_fire_visual(img) == True:
            pxes = track_fire_visual(img)
            for px in pxes:
                p1 = Point(px,"visual2gps")
                pt_cam = common.coordinate.get_line_plane_intersection(p1.visual,self.init.init_pt.visual)
                # TODO: Implement the flag in the coordinate
                pt = Point(pt_cam,"visual_cam2gps")
                self.p.append(pt.gps)

    '''
    '''
    def export_fire_location(self):
        return self.p

    