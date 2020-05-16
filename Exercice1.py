#coding:utf8

#Ecrire un programme qui saisit deux entiers a et b,
#calcule et affiche le quotient entier, le reste de la division et le ratio (quotient réel)

print("Entrer deux variables a et b")
a=int(input())
b=int(input())
print("Quotient entier= ", int(a/b))
print("Reste= ", a%b)
print("Quotient reel= ", float(a/b))
