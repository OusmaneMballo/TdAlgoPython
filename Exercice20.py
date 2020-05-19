#coding:utf8
"""
Ecrire un algorithme qui demande successivement 10 nombres à l'utilisateur, 
et qui affiche à la fin le plus grand de ces 10 nombres Et affiche aussi 
son rang dans la liste saisie
"""
max = 0
T=[]
for i in range(0 , 10):
    print("Entrer la valeur",i)
    T.append(int(input()))
    if T[i] > max:
        max = T[i]
        j = i
print("La valeur maximale est de ",max," a la position",j)
print(T)
