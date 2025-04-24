def compare(liste,liste2):
    commun = []
    for i in range(len(liste)):
        for j in range(len(liste2)):
            if liste[i] == liste2[j]:
                if liste[i] not in commun:
                    commun.append(liste[i])
    return commun


nbListe =input("Donner une liste de nombre ex(1,2,3): ")
nbListe2 =input("Donner une deuxieme liste de nombre : ")

liste = nbListe.split(",")
liste2 = nbListe2.split(",")

communs = compare(liste,liste2)

print("Communs : ",communs)
