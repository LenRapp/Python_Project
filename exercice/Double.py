def estDoublon(liste):
    doublon=[]
    for i in range(len(liste)):
        for j in range(i):
            if liste[i] == liste[j]:
                doublon.append(liste[i])
    return doublon


nb=(input("Donner une liste de nombre ex(1,2,3): "))

nb = nb.split(",")

doublons = estDoublon(nb)

print("Voici les doublons :",doublons)

