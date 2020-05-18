#coding:utf8
"""
Ecrire l’algorithme qui affiche la somme des prix d'une suite d'articles en CFA (entiers)
saisies par l'utilisateur et se terminant par zéro.
"""
som=0
while True:
    print("Entrer un prix, sinon entrer 0 pour quitter")
    prix=int(input())
    if prix !=0 :
        som = som + prix
    if prix == 0:
        break
print("La somme de vos article est de: ",som)
