#coding:utf8
"""
Ecrire un programme qui saisit un réel x et un entier n et affiche x à la puissance n.
Version 1 : utiliser la fonction pow  du fichier d’en-tête <math.h>  ex : pow(x,n)
"""
#Resolution V1:
"""
print("Entrer un entier x")
x=int(input())
print("Enter sa puissance n")
n=int(input())
print(x,"^",n,"=",pow(x,n))
"""
#Resolution V1:
"""
Calcul la puissance en utilisant une boucle
"""

print("Entrer un entier x")
x = int(input())
print("Enter sa puissance n")
n = int(input())
val=x
for i in range(1,n):
    val=val*x
print(x, "^", n, "=",val)
