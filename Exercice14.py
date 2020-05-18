#coding:utf8
"""
Faire un programme qui saisit une date (jour, mois et année) at qui indique 
si l’année est bissextile 
"""
print("Entrer une date jj/mm/an")
j=int(input())
m=int(input())
an=int(input())
if(an % 4==0):
   print("La date",j,"/",m,"/",an," est bissextile")
else:
    print("La date",j,"/",m,"/",an," n'est pas bissextile")
