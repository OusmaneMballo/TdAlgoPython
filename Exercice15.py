#codin:utf8
"""
Ecrire un algorithme qui demande un nombre de départ, et qui calcule la somme 
des entiers jusqu'à ce nombre. Par exemple si l'on tape 4 , 
l’algorithme doit calculer: 1 + 2 + 3+ 4 = 10 Réécrire l'algorithme qui calcule
 cette fois la moyenne !
"""
print("Entrer un nombre")
x=int(input())
som=0
for i in range(1,(x+1)):
    som=som+i
print("La somme des nombres comprisent entre 1 et ",x," est de ",som)