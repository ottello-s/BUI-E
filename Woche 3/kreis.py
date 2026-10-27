import math


class Kreis:
    def __init__(self, r):
        self.radius = r

    def berechne_umfang(self):
        return 2 * math.pi * self.radius
    
    def get_radius(self):
        return self.__radius

    def set_radius(self, ra):
        if ra >= 0:
            self.__radius = ra
        else:
            print("Radius < 0", ra)
            self.__radius = 0
    


    radius = property(get_radius,set_radius)


    
kreis_1 = Kreis(1)
kreis_2 = Kreis(-2)

umfang_1 = kreis_1.berechne_umfang()
print(umfang_1)
umfang_2 = kreis_2.berechne_umfang()
print(umfang_2)
