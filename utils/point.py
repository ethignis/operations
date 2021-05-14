from coordinate import gps2world
'''
A class for each GPS point. The class essentially capsulates both
geo-coordinate and cartesian coordinate of the point such that
both could be kept in the same place
'''
class Point:
    def __init__(self,lat,lng):
        self.gps = [lat,lng]
        self.pos = gps2world(lat,lng)

    def get_gps(self):
        return self.gps

    def get_pos(self):
        return self.pos