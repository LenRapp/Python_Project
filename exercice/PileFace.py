import random

def lancerPiece():
    piece = random.randint(1, 2)
    if piece == 1:
        return "Pile"
    else:
        return "Face"

def choix():
    print("Choisis pile ou face :")
    choix = input("Ton choix : ")
    return choix

def verif_gagnant(user_choix, tirage):
    if user_choix.lower() == tirage.lower():
        return True
    else:
        return False

# Programme principal
user = choix()
tirage = lancerPiece()

print("La pièce est tombée sur :", tirage)

if verif_gagnant(user, tirage):
    print("Bravo tu as gagné !")
else:
    print("Perdu !")
