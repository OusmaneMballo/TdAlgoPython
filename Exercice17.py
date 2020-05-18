#codin:utf8
"""
Faire un programme qui calcule le PGCD de deux nombres saisis au clavier en utilisant
l'astuce suivante: soustrait le plus petit des deux entiers du plus grand 
jusqu'à ce qu'ils soient égaux.
"""
print("Entrer deux entiers")
x=int(input())
y=int(input())
if x > y:
    while True:
        x = x - y
        if x <= y:
            break
    print("Le PGCD est de",x)
else:
    while True:
        y = y - x
        if y <= y:
            break
    print("Le PGCD est de ",y)
