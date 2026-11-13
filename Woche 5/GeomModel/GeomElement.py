import abc


class GeomElement(abc.ABC):
    """abstract class for all derived geom elements """
   
    # define the constructor as abstract -> no instance of this class can be created
    @abc.abstractmethod
    def __init__(self):
        pass
    





