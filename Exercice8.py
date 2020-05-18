#coding:utf8
from math import *
"""
 Ecrire un algorithme permettant de résoudre une équation du second degré. 
"""
print("Entrer la valeur de a")
a=int(input())
print("Entrer la valeur de b")
b = int(input())
print("Entrer la valeur de c")
c = int(input())
if((a==0 and b==0) or (a==0 and c==0) or (b==0 and c==0)):
    print("Impossible, pas de solution")
else:
    if a!=0:
        d=(b**2)-(4*(a*c))
        if d<0:
            print("Pas de solution!")
        else:
            if d == 0:
                print("On a une seule solution unique")
                print("X0=", (-b / (2 * a)))
            else:
                print("On a deux solutions")
                print("X1=",(-b - sqrt(d)) / (2 * a))
                print("X2=", (-b + sqrt(d)) / (2 * a))
    else:
        print("On a une seule solution")
        print("X=",-c/b)
