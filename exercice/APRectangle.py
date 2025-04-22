def aire(largeur, longeur):
    return largeur * longeur

def perimetre(largeur, longeur):
    return 2 * (largeur + longeur)

largeur = int(input("Entrez la largeur : "))
longeur = int(input("Entrez la longeur : "))

print("L'aire du rectangle est : ", aire(largeur, longeur))
print("Le perimetre du rectangle est : ", perimetre(largeur, longeur))