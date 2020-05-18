#coding:utf8
"""
Un nombre est parfait s’il est égal à la somme de ses diviseurs stricts 
(différents de lui-même). Ainsi par exemple, l’entier 6 est parfait car 6 = 1 + 2 + 3. 
Écrire un algorithme permettant de déterminer si un entier naturel est un nombre parfait.
"""
print("Entrer un nombre")
x=int(input())
som=0
for i in range(1,(x-1)):
    if x % i == 0:
        som = som + i
if som == x:
    print(x," est un nombre parfait")
else:
    print("Oups!... ",x," n'est pas un nombre parfait")