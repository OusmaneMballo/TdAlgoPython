#coding:utf8
"""
La multiplication des lapins. Vous allez faire l’acquisition d’un couple de bébés lapins. 
Au bout d’un mois ce couple est adulte. Le mois suivant il donne naissance à un couple 
de bébés lapins : vous avez maintenant 4 lapins. Puis chaque couple engendre tous les mois 
un nouveau couple deux mois après sa naissance. 
"""
x0=2
x1=2
for i in range(0,(12-2)):
    NL = x1+x0
    x0 = x1
    x1 = NL

print("A la premiere  annee vous aurrez ",NL," lapins")
NL = 0
x1 = 2
x0 = 2
i = 1
while True:
    NL = x1+x0
    x0 = x1
    x1 = NL
    i +=1
    if NL >= 1000000000:
        break
print("Vous aurrez 1000000000 de lapin a la",i,"eme annes!")
