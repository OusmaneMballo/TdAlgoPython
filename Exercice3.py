#conding:utf8

"""
Version 1 :
Faire un programme qui saisit 3 résistances : R1, R2 et R3.
Calculer et afficher la résistance en série : R1 + R2 +R3
Calculer et afficher la résistance en parallèle : (R1 * R2 * R3) / (R1*R2 + R2*R3 + R1*R3)
VERSION 1
"""
"""
print("Entrer la valeur de R1")
r1=float(input())
print("Entrer la valeur de R2")
r2=float(input())
print("Entrer la valeur de R3")
r3 = float(input())
print("La resitence parallele est de: ",
      (r1 * r2 * r3) / ((r1 * r2) + (r2 * r3) + (r1 * r3)))
      """
#VERSION 2
"""
Version 2 :
Demander a l’utilisateur d’indiquer son choix.
S’il entre la valeur  1, calculer et afficher la fréquence en série.
S’il entre la valeur 2, calculer et afficher la fréquence en parallèle.
"""
print("Entrer la valeur de R1")
r1 = float(input())
print("Entrer la valeur de R2")
r2 = float(input())
print("Entrer la valeur de R3")
r3 = float(input())
while True:
    print("1-Calcul frequence parallele")
    print("2-Calcul frequence serie")
    choix=int(input())
    if (choix==1 or choix==2):
        break
if choix==1:
    print("La resitence parallele est de: ",
          (r1 * r2 * r3) / ((r1 * r2) + (r2 * r3) + (r1 * r3)))
else:
    print("La resitence serie est de: ", r1 + r2 + r3)
