#coding:utf8
"""
Ecrire un programme qui saisit 5 variables de type entier au clavier 
et qui affiche leur somme. Utiliser une boucle (for ou while ou do..while).

"""
x=0
for i in range(0,5):
    print("Entrer un entier")
    x=x+int(input())

print("La somme de tes variables est de : ",x)

