import random

while True:
    nbLancer = int(input("Combien de lancer de dés : "))
    nbFaces = int(input("Combien de faces : "))

    resultat = []
    for i in range(nbLancer):
        resultat.append(random.randint(1, nbFaces))
    somme = 0
    for e in resultat:
        somme += e
    print("Résultats des lancers : ", resultat)
    print("Somme :", somme)
    # ici on utiilse la methode sum directement
    #print("Somme :", sum(resultat))

    relancer = str(input("Tu veux relancer (y/n) :")).lower()
    if relancer != 'y':
        print("Fin du Jeu")
        break