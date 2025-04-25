def inverseListe(liste):
    listeInv = []
    for i in range(len(liste)):
        listeInv.append(liste[len(liste)-i-1])
    return listeInv

chaine=input("Donner une liste de nombre : ")

inverse = inverseListe(chaine)

print("Voici l'inverse :",inverse)