import math

class Kreis:
    def __init__(self,r):
        self.radius = r 

    def berechne_umfang(self):
       return 2 * math.pi * self.radius


kleiner_Kreis = Kreis(2)

grosser_Kreis = Kreis(10)

print("Umfang kleiner Kreis")
print(kleiner_Kreis.berechne_umfang())