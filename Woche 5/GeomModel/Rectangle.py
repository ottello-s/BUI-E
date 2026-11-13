from GeomElement2D import GeomElement2D


class Rectangle(GeomElement2D):
    """ instantiable class representing a rectangular 2D shape """

    # constructor
    def __init__(self, length: float, height: float):
        print('create an instance of class Rectangle')
        self.length: float = length
        self.height: float = height

    # implement calc_area() method requested by the parent GeomElement2D class
    def calc_area(self) -> float:
        return self.length * self.height

    # implement calc_perimeter() method requested by the parent GeomElement2D class
    def calc_perimeter(self) -> float:
        return 2 * (self.length + self.height)


