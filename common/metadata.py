'''
Functions needed when starting the initial flight
PLEASE CALL THIS FUNCTION WHEN THE FLIGHT STARTS SUCH THAT
GROUND INFORMATION COULD BE COLLECTED!!!!!
'''
from data.vtol import get_current_location
from point import Point

class MetaData:
    def __init__(self,gps):
        self.init_gps = gps # Pt - GPS location of the initial starting point 
    
