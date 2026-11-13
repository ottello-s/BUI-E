from GeomElement2D import GeomElement2D
import math

class RectangularTriangle(GeomElement2D):
    def __init__(self,leg_A:float,leg_B:float):
        print("Creating an instance of class RecTriangle")
        self.leg_A:float = leg_A
        self.leg_B:float = leg_B

    def calc_area(self):
        return self.leg_A * self.leg_B * 0.5


    def calc_perimeter(self):   
        return (self.leg_A**2 + self.leg_B**2)**0.5 + self.leg_A + self.leg_B

    def is_valid_geometry(self):
        angle1 = math.degrees(math.atan(self.leg_A / self.leg_B))
        angle2 = math.degrees(math.atan((self.leg_A**2 + self.leg_B**2)**0.5 / self.leg_B))


        if angle1 < 150 and angle2 < 150:
            print("Great Success")
            return True
        else:
            ValueError


        