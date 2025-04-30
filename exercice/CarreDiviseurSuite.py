def carre(n):
    return n*n

def diviseur(n):
    diviseurs = []
    for i in range(1,n+1):
        if n%i == 0:
            diviseurs.append(i)
    return diviseurs

n=int(input("Entrez un nombre : "))

#for i in range(1,n+1): si on veut tous les resultat jusqua l'entier donner
# ex "Entrez un nombre : 3" il donnera le resultat de 1,2 et 3
c=carre(n)
d=diviseur(c)
print("n =", n, ": carré =", c, ", diviseurs =", d)