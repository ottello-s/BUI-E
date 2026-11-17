import random


liste = []

for i in range (10):
    n = random.randint(1, 100)
    liste.append(n)
print(f"Liste: {liste}")

listeinv = liste[::-1]
print(f"Invertierte Liste: {listeinv}")

def dist(liste):
    listedist = []
    for i in range(len(liste)):
        if i < len(liste)-1:
            n = abs(liste[i+1] - liste[i])
        else:
            n = abs(liste[i] - liste[i-1])
        listedist.append(n)
    print(f"Distanzen: {listedist}")
    return listedist

listdist = dist(liste)

def maxdist(liste):
    listemax = []
    for i in range(len(liste)):
        if i < len(liste)-1:
            n = abs(liste[i+1] - liste[i])
        else:
            n = abs(liste[i] - liste[i-1])
        listemax.append(n)
    return max(listemax)


def mindist(liste):
    listemin = []
    for i in range(len(liste)):  
        if i < len(liste)-1:
            n = abs(liste[i+1] - liste[i])
        else:
            n = abs(liste[i] - liste[i-1])
        listemin.append(n)
    return min(listemin)

print(f"Minimale Distanz: {mindist(liste)}, Maximale Distanz: {maxdist(liste)}")


werten = [ [1,2], [3,4],

          [5,6],

          [7,8],

          [9,10]    ]

for g in werten():
    for a in g: 
    print (g)







matrix = [
    [i, l, listdist[i] ]
    for i, l in enumerate(liste)
    ]
print(f"Matrix: {matrix}")

matrix2 = []
for i in range(len(liste)):
    matrix2.append([i, liste[i], listdist[i]])
print(f"Matrix2: {matrix2}")