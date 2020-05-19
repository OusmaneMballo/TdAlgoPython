#coding:utf8
"""
On se propose de saisir N entiers différents entre 1 et 100 
(N étant un entier naturel compris entre 10 et 50) puis afficher la plus longue séquence 
croissante tout en précisant la position du premier nombre de cette séquence.
Exemple : Pour N=15
"""

while True:
    print("Entrer un entier N compris entre 10-50")
    N=int(input())
    if N>=10 and N<=50:
        break
T=[]
for i in range(0,N):
    print("Entrer un entier")
    T.append(int(input()))

for i in range(0,N):
    if i==1:
        deb = 1
        svg = 0
    if T[i]>T[i+1] or i==N :
        if svg < (i-deb) :
            svg = i-deb
        
        deb = i+1
print("La plus longue sequence est:")
for i in range(deb, (deb+svg)):
    print(T[i],"*")

print("Qui debut a la position”,deb,” et qui a pour longeur",deb+svg)

