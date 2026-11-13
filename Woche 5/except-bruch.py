import sys 

def teilen(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("Error")
    finally:    
        print("func done")
        return c

zahlA = float(input("Zaehler eingeben: "))
zahlB = float(input("Nenner eingeben: "))

print(teilen(zahlA,zahlB))