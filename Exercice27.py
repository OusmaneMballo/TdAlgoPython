#coding:utf8
"""
Faire un programme qui saisit une suite de nombre et qui dit les si les nombres saisis sont
 dans l’ordre croissant ou décroissant ou quelconque.
"""
i = 1
T=[]
while True:
    print("Tapez sur 0 pour quitter")
    print("Entrer un nombre")
    x = int(input())
    i+=1
    if x==0:
        break

    T.append(x)

for j in range(len(T)):
    if j==0 :
        if T[j]<T[j+1]:
            val = 1
        else:
            val = 0
    else:
        if val==1:
            if T[j]>T[j+1]:
                val = 2
                j = i
        else:
            if T[j]<T[j+1]:
                val = 2
                j = i

if val==1:
    print("Vous avez donnes une suite de nombre croissantes")
else:
    if val==0:
        print("Vous avez donnez une suite de nombre decroissantes ")
    else:
        print("Vous avez donnes une suite de nombre quelconque")
