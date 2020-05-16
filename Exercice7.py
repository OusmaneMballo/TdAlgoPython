#coding:utf8
"""
Décomposition d’un montant en euros Écrire un algorithme permettant 
de décomposer un montant entré au clavier en billets de 20, 10, 5 euros 
et pièces de 2, 1 euros, de façon à minimiser le nombre de billets et de pièces.
"""
print("Entrer un montant")
montant=int(input())
print("Decomposition")
print("-------------")
while montant >= 1:
    if montant > 20:
        print("20")
        montant=montant-20
    if montant >= 10:
        print("10")
        montant=montant-10
    if montant >= 5:
        print("5")
        montant = montant - 5
    if montant > 2:
        print("2")
        montant = montant - 2
    if montant >=1:
        if montant == 1:
            print("1")
            montant = montant - 1
        else:
            print("1")
            montant = montant - 1
