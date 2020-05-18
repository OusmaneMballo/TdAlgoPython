#coding:utf8
"""
 Faire un programme qui saisit une date (jour, mois et année)
 et qui indique si la date est valide
"""
print("Entrer une date jj/mm/an")
j=int(input())
m=int(input())
an=int(input())
if(j<=0 or j>31 or m<=0 or m>12):
    print("La date",j,"/",m,"/",an,"est invalide")
else:
    if(an % 4==0):
        if(m==2 and j>29):
            print("La date", j, "/", m, "/", an, "est invalide")
        else:
            if(m!=8 and (m % 2==0) and j>30):
                print("La date", j, "/", m, "/", an, "est invalide")
            else:
                if(m==8 and (m % 2!=0) and j>31):
                    print("La date", j, "/", m, "/", an, "est invalide")
                else:
                    print("La date", j, "/", m, "/", an, "est valide")
    else:
        if(m==2 and j>28):
            print("La date", j, "/", m, "/", an, "est invalide")
        else:
            if(m!=8 and (m % 2==0) and j>30):
                print("La date", j, "/", m, "/", an, "est invalide")
            else:
                if(m==8 and (m % 2!=0) and j>31):
                    print("La date", j, "/", m, "/", an, "est invalide")
                else:
                    print("La date", j, "/", m, "/", an, "est valide")
