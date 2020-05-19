#coding:utf8
"""
Ecrire un algorithme mettant en œuvre le jeu suivant entre deux joueurs : 
Le premier utilisateur saisi un entier que le second doit deviner. 
Pour cela, il a le droit à autant de tentatives qu'il souhaite. 
A chaque échec, le programme lui indique si l'entier est plus grand ou plus petit 
que sa proposition. Un score est affiché lorsque l'entier est trouvé.
"""

print("JOUEUR1: Entrer le nombre a deviner!")
x=int(input())
score = 10
while True:
    if score==0 :
        print("GAME OVER!!!")
        print("Vous avez perdu!")
        break
    print("JOUEUR2: Deviner le nombre cacher!")
    val=int(input())
    if val==0:
        break
    if val<x:
        print("Oups!... le nombre est plus grand que ce que vous avez saisi, Appuiez sur 0 pour quitter")
        score -= 1
    else:
        if val>x :
            print("Oups!... le nombre est plus petit que ce que vous avez sais, Appuiez sur 0 pour quitteri")
            score -= 1
        else:
            print("FELLICITATION!!!!! vous avez devinez le nombre cacher!...")
            print("SCORE:",score)
            break
