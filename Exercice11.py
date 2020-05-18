#coding:utf8
"""
Ecrire un algorithme calculatrice permettant la saisie du premier entier (a) 
de l'opération ( + ou – ou * ou / : sont des caractères) et du deuxième entier (b) 
et qui affiche le résultat.
"""
while True:
    print("Entrer le premier entier")
    a = int(input())
    print("Entrer le deuxieme entier")
    b = int(input())
    print("Indiquer l'operateur")
    op = input()
    if op == '*':
        print(a,"*",b," = ",a*b)
        break
    else:
        if op == "/":
            if b == 0:
                print("Impossible de diviser par 0")
                break
            else:
                print(a,"/",b," = ",a/b)
                break
        else:
            if op == "+":
                print(a,"+",b," = ",a+b)
                break
            else:
                if op == "-":
                    print(a, "-", b, " = ", a - b)
                    break
                else:
                    print("Oups!... operateur incorrecte!")
                    print("Exemple d'operateur: *, +, /, -")
