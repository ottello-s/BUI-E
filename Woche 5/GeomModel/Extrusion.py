from GeomElement3D import GeomElement3D
from GeomElement2D import GeomElement2D



class Extrusion(GeomElement3D):
     
     def __init__(self, cross_section: GeomElement2D, extrusion_height:float):
            print('create an instance of class Extrusion')
            super().init()

            self.cross_section = cross_section
            self.extrusion_height = extrusion_height

    def calc_volume(self)-> float:
      return self.cross_section*self.extrusion_height