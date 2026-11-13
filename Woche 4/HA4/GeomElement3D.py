from abc import abstractmethod
from GeomElement import GeomElement

class GeomElement3D(GeomElement):

    @abstractmethod
    def __init__(self):
        pass

    def calc_volume(self):
        """This one calcs Volume of your 3D Geometry"""
        pass 

    @abstractmethod
    def is_valid_geometry(self):
        """This one checks if ur 3D Geometry is valid"""
        pass 