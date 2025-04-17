nb=int(input("Entrer un entier : "))
nbChaine = str(nb)
somme = 0
liste_chiffre = []
for e in nbChaine:
    liste_chiffre.append(e)
    somme += int(e)
calcule = " + ".join(liste_chiffre)
print("La somme de ses chiffres est",calcule,"=",somme)


