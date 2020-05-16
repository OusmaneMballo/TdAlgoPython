#coding:utf8
from math import *
"""
Faire un programme qui saisit  les coordonnées de 2 points 
A (x1, y1) et b(x2, y2) et qui affiche la distance entre les 2 points.
Formule : distante = racine carrée de ((x1 – x2)2  + (y1 – y2)2)
Racine carrée : sqrt. Ex : sqrt(7) ; <math.h>
"""
print("Entrer les coordonnees du point A")
print("A(X1)")
x1=float(input())
print("A(y1)")
y1 = float(input())
print("Entrer les coordonnees du point B")
print("B(X2)")
x2 = float(input())
print("B(y2)")
y2 = float(input())
val = (x1 - x2) * 2 + (y1 - y2) * 2
if val>0:
    print("Distance(AB)= ", sqrt(val))
else:
    print("Les deux points A et B sont confondu")
