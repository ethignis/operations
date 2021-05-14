from vtol import get_current_location
import 
'''
Functions needed when starting the initial flight
PLEASE CALL THIS FUNCTION WHEN THE FLIGHT STARTS SUCH THAT
GROUND INFORMATION COULD BE COLLECTED!!!!!
'''
class MetaData:
    def __init__(self):
        self.init_pt = Point(get_current_location())
        self.init_height = 
    def get_init_height(self):
        self.init_height = get 
