#coding:utf8
"""
Ecrire un algorithme qui lit trois valeurs entières ( A, B et C)
et qui permet de les trier par échanges successifs Et enfin les afficher dans l'ordre 4.
"""
print("Donner la valeur de A")
a=int(input())
print("Donner la valeur de B")
b=int(input())
print("Donner la valeur de C")
c = int(input())
if a>b:
    if a>c:
        if b>c:
            print("Affichage par ordre decroissant:", a, b, c)
        else:
            print("Affichage par ordre decroissant:", a, c, b)
    else:
        print("Affichage par ordre decroissant:", c, a, b)
else:
    if b>c:
        if a>c:
            print("Affichage par ordre decroissant:", b, a, c)
        else:
            print("Affichage par ordre decroissant:", b, c, a)
    else:
        print("Affichage par ordre decroissant:", c, b, a)
