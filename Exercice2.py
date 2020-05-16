#coding:utf8

"""Ecrire un programme qui demande à l’utilisateur de donner le rayon d’un cercle 
et lui retourne sa surface et son périmètre. 
PI =  4 * arc tangeante de 1. la fonction arc tangeante est atan ex : atan(2).
perimetre du cercle=2pi*r"""

print("Entrer le rayon du cercle")
r=float(input())
print("Surface= ",3.14*(r**2))
print("Perimetre= ",2*3.14*r)
