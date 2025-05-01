def transformer(n):
    liste= []
    i=0
    while i < 3:
        r = n%10
        n = n//10
        liste = [r] + liste
        i+=1
    return liste

def calcul(liste):
    somme = liste[0] - liste[1]
    return somme

n=int(input("Entrer un nombre à 3 chiffres: "))
liste = transformer(n)
calculs = calcul(liste)
dernier = liste[2]
print("Le dernier chiffre est", dernier)
print("Le calcul est", calculs)
if calculs == dernier:
    print("C'est un nombre particulier")
else:
    print("Ce n'est pas un nombre particulier")


