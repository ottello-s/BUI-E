import abc
from GeomElement import GeomElement


class GeomElement2D(GeomElement):
    """ abstract base class for all 2D types of geometry """ 

    # define the constructor as abstract -> no instance of this class can be created
    @abc.abstractmethod
    def __init__(self):
        pass

    # define calc_area, must be implemented by all derived classes
    @abc.abstractmethod
    def calc_area(self) -> float:
        """ calculates the area of this 2D geometry"""
        pass

    # define calc_perimeter, must be implemented by all derived classes
    @abc.abstractmethod
    def calc_perimeter(self) -> float:
        """ calculates the perimeter of this 2D geometry"""
        pass
