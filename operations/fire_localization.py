'''
This operation is used to localize the location of the fire such that 
fires could be marked on the map
'''

import numpy as np
import data.vtol
from common.metadata import MetaData
from common.point import Point
import common.coordinate
import fire_detection

class FireLocalizer:
    def __init__(self):
        '''
        '''
        self.init = MetaData()
        self.p = []

    def localize_fire_thermal(self):
        img = self.get_image()
        if fire_detection.detect_fire_thermal(img) == True:
            pxes =  fire_detection.track_fire_thermal(img)
            for px in pxes:
                # px_cam = common.coordinate.img2thermal_cam(px,2)
                # pt_cam = common.coordinate.get_line_plane_intersection(px_cam,self.init.init_pt)
                # pt_body = common.coordinate.thermal_cam2body(pt_cam)
                # pt_world = common.coordinate.body2world(pt_body)
                # pt_gps = common.coordinate.world2gps(pt_world)
                # pt = Point(pt_gps[0],pt_gps[1],self.init.init_height)
                p1 = Point(px,"thermal2gps")
                pt = common.coordinate.get_line_plane_intersection(p1.thermal,self.init.init_pt.thermal)
                self.p.append(pt)

    def localize_fire_visual(self):
        img = self.get_image()
        if fire_detection.detect_fire_visual(img) == True:
            pxes = fire_detection.track_fire_visual(img)
            for px in pxes:
                px_cam = common.coordinate.img2visual_cam(px,2)
                pt_cam = common.coordinate.get_line_plane_intersection(px_cam,self.init.init_pt)
                pt_body = common.coordinate.visual_cam2body(pt_cam)
                pt_world = common.coordinate.body2world(pt_body)
                pt_gps = common.coordinate.world2gps(pt_world)
                pt = Point(pt_gps[0],pt_gps[1],self.init.init_height)
                self.p.append(pt)

    '''
    '''
    def export_fire_location(self):
        pass
