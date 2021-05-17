'''
Functions needed when starting the initial flight
PLEASE CALL THIS FUNCTION WHEN THE FLIGHT STARTS SUCH THAT
GROUND INFORMATION COULD BE COLLECTED!!!!!
'''
from data.vtol import get_current_location
from point import Point

class MetaData:
    def __init__(self):
        self.init_pt = Point(get_current_location(),"init")
        self.init_height = self.init_pt[-1]
    
