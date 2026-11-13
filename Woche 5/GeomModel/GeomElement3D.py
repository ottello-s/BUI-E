import abc

from GeomElement import GeomElement

class GeomElement3D(GeomElement):
    """ abstract base class for all 3D types of geometry """

    # constructor stays abstract -> no instance of this class can be created
    @abc.abstractmethod
    def __init__(self):
        pass

    # must be implemented by all derived classes
    @abc.abstractmethod
    def calc_volume(self) -> float:
        """ calculates the volume of this 3D geometry """
        pass
