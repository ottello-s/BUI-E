from GeomElement3D import GeomElement3D


class Cuboid(GeomElement3D):
    def __init__(self, length:float, height:float, width:float):
        self.length:float = length
        self.height:float = height
        self.width:float = width

    def calc_volume(self):
        return  self.length *  self.height *  self.width


    def is_valid_geometry(self):
        return 