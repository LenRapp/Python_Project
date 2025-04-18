nbUser=(input("Enter des nombres séparés par une virgules :"))
nb_separer = nbUser.split(",")
l=[]
for i in nb_separer:
    l.append(int(i))

print("Résultat de l'analyse :")
print("La moyenne :",sum(l)/len(l))
print("La somme :",sum(l))
print("Le plus grand nombre :",max(l))
print("Le plus petit nombre :",min(l))
print("Le nombre total d'élément :",len(l))