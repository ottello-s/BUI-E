from fahrpreisberechnung import ermittle_preis

testCheck = {
    "AB": 8.0,
    "CI": 1.6,
    "DH": 8.0,
    "FC": 9.6,
    "BE": 3.2,
    "FG": 4.8
}

testRun = {
    "AB": ["A","B", False],
    "CI": ["C","I", False],
    "DH": ["D","H", True],
    "FC": ["F","C", True],
    "BE": ["B","E", False],
    "FG": ["F","G", False]
}

def tester():
    for i, j in testRun.items():
        erwartet = testCheck[i]
        erhalten = ermittle_preis(j[0],j[1],j[2])
        if erwartet == erhalten:                                                                
            print(i, "richtig!")
        else:
            print(i, "falsch", "Erwartet:", erwartet, "Erhalten:", erhalten)
    return

tester()