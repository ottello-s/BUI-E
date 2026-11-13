from abc import abstractmethod
from GeomElement import GeomElement

class GeomElement2D(GeomElement):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calc_area(self):
        """Calculates the are of this 2D Geometry"""
        pass