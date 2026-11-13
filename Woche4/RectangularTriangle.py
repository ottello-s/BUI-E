from GeomElement2D import GeomElement2D

class RectangularTriangle(GeomElement2D):

    def __init__(self, leg_a, leg_b):
        print("Creating an instance of class RectangularTriangle")
        self.leg_a = leg_a
        self.leg_b = leg_b

    def calc_area(self):
        return 0.5 * self.leg_b * self.leg_a