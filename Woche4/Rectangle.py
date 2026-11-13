from GeomElement2D import GeomElement2D

class Rectangle(GeomElement2D):

    def __init__(self, length: float, height: float):
        print("Creating an instance of class Rectangle")
        self.length: float = length
        self.height: float = height

    def calc_area(self):
        return self.length * self.height