import random 

def preis_von_bis(zone_ab, zone_bis):
    preis_von_bis = 0

    if zone_ab > zone_bis:
        zone_klein = zone_bis
        zone_gross = zone_ab
    else:
        zone_klein = zone_ab
        zone_gross = zone_bis

    preis_von_bis = 1.60*(zone_gross - zone_klein + 1)
    # mindestpreis fuer die Fahrt innerhalb einer Zone
    return preis_von_bis

ermittle_zone = {
                "A" : 5,
                "B" : 1,
                "C" : 4,
                "D" : 3,
                "E" : 2,
                "F" : 3,
                "G" : 5,
                "H" : 3,
                "I" : 4,
                "J" : 5
                }



def ermittle_preis(halte_anf, halte_end, zentrum):
    # halte_anf = input("von welcher Haltestelle? ").upper()
    # halte_end = input("bis zu welcher Haltestelle? ").upper()
    # zentrum = input(" durch das Zentrum? [ja/nein]").lower() == "ja"   

    print("Start:", halte_anf)  
    print("End:", halte_end)
    print("Zentrum: Ja" if halte_anf else "Zentrum: Nein")

    zone_anf = ermittle_zone[halte_anf]
    zone_end = ermittle_zone[halte_end]

    if not zentrum:
        preis = preis_von_bis(zone_anf, zone_end)
    else: 
        preis = preis_von_bis(zone_anf, 1) + preis_von_bis(1, zone_end) - 1.60
    print(preis)
    return preis 


# ermittle_preis()

