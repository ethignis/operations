from . import coordinate
import numpy as np
import geojson
from geojson import Point, Feature, FeatureCollection, dump

'''
@TODO: use geojson and pygdal to support the export of geolocations 
       in the format of geojson to enable Formant to run the program
'''
'''
A class for each GPS point. The class essentially capsulates both
geo-coordinate and cartesian coordinate of the point such that
both could be kept in the same place
'''
class Point:
    def __init__(self,x,angle,flag,init):
        '''
        flag == "gps2visual" => GPS -> visual image
        flag == "gps2thermal" => GPS -> thermal image
        flag == "visual2gps" => visual image -> GPS
        flag == "thermal2gps" => thermal image -> GPS
        flag == "init" => point for initial metadata
        flag == "thermal_cam2body" => cam -> body -> gps
        flag == "visual_cam2body" => cam -> body -> gps
        '''
        # Angle with respective to north as x and east as y (NED) 
        self.dir_angle = get_direction()

        if flag == "gps2visual":
            self.gps = np.array(x)
            self.world = coordinate.gps2world(self.gps)
            self.body = coordinate.world2body(self.world,angle,init)
            self.visual = coordinate.body2visual_cam(self.body)
            self.visual_img = coordinate.visual_cam2img(self.visual)
        elif flag == "gps2thermal":
            self.gps = np.array(x)
            self.world = coordinate.gps2world(self.gps)
            self.body = coordinate.world2body(self.world,angle,init)
            self.thermal = coordinate.body2thermal_cam(self.body)
            self.thermal_img = coordinate.thermal_cam2img(self.visual)
        elif flag == "visual2gps":
            self.visual_img = np.array(x)
            self.visual = coordinate.img2visual_cam(self.visual_img)
            self.body = coordinate.visual_cam2body(self.visual)
            self.world = coordinate.body2world(self.body,angle,init)
            self.gps = coordinate.world2body(self.world)
        elif flag == "thermal2gps":
            self.thermal_img = np.array(x)
            self.thermal = coordinate.img2thermal_cam(self.thermal_img)
            self.body = coordinate.thermal_cam2body(self.thermal)
            self.world = coordinate.body2world(self.body,angle,init)
            self.gps = coordinate.world2body(self.world)
        elif flag == "init":
            self.gps = np.array(x)
            self.world = coordinate.gps2world(self.gps)
            self.body = coordinate.world2body(self.world,angle,init)
            self.visual = coordinate.body2visual_cam(self.body)
            self.visual_img = coordinate.visual_cam2img(self.visual)
            self.thermal = coordinate.body2thermal_cam(self.body)
            self.thermal_img = coordinate.thermal_cam2img(self.visual)
        elif flag == "thermal_cam2body":
            pass
        elif flag == "visual_cam2body":
            pass

'''
@function: export the GPS position of the point to the GeoJSON
@param: pt - a Point class 
@
'''
def export_point(pt,count):

    point = Point(pt.gps)

    features = []
    features.append(Feature(geometry=point, properties={"country": "Spain"}))

    # add more features...
    # features.append(...)

    feature_collection = FeatureCollection(features)

    with open('location-{}.geojson'.format(count), 'w') as f:
        dump(feature_collection, f)