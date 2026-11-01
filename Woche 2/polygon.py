

punkte = [
    [0, 2],
    [2,2],
    [2, 0],
    [0, 0]
]

print(punkte)

def polygon(punkte = []):
    umfang = 0
    flaeche = 0
    uhrzeigesinn = False

    if len(punkte) >= 3:
        punkte.append(punkte[0])

        """UMFANG"""
        for i in range(len(punkte)-1):
            print(umfang)
            umfang += ((punkte[i+1][0] - (punkte[i][0]))**2 + (punkte[i+1][1] - punkte[i][1])**2)**0.5

        """FLAECHE"""
        for i in range(len(punkte)-1):
            flaeche += 0.5*(punkte[i][0]-punkte[i+1][0])*(punkte[i][1]+punkte[i+1][1])

        """UHRZEIGESINN"""
        uhrzeigesinn = flaeche >= 0

    else: 
        umfang, flaeche = 0
        print("<3 Eckpunkte")


    return umfang, flaeche, uhrzeigesinn 

umfang, flaeche, uhrzeigesinn = polygon(punkte)
print(f"Flaeche: {abs(flaeche)}")
print(f"Umfang: {umfang}")
print("gegen Uhrzeigersinn" if uhrzeigesinn else "Uhrzeigersinn") 
