#coding:utf8
"""
Faire un programme qui calcule et affiche la division de a par b par soustractions 
successives
"""
print("Entrer a")
a=int(input())
print("Entrer b")
b = int(input())
val=a
nbr=0
while a / b != nbr:
    nbr=val-b
    val=val-1
print(a,"/",b,"= ",nbr," par division soustraction")

