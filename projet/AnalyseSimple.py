nbUser=(input("Enter des nombres séparés par une virgules :"))
nb_separer = nbUser.split(",")
l=[]
for e in nb_separer:
    l.append(int(e))


# Version avec des fonctions
def somme():
    som = 0
    for i in range(len(l)):
        som += l[i]
    return som

def maxNb():
    maxi = 0
    for i in range(len(l)):
        if l[i] > maxi:
            maxi = l[i]
    return maxi
def minNb():
    mini = l[0]
    for i in range(len(l)):
        if l[i] < mini:
            mini = l[i]
    return mini


print("Résultat de l'analyse :")
print("La moyenne :",somme() / len(l))
print("La somme :",somme())
print("Le plus grand nombre :",maxNb())
print("Le plus petit nombre :",minNb())
print("Le nombre total d'élément :",len(l))

# Version simple en utilisant les methodes de python

# print("Résultat de l'analyse :")
# print("La moyenne :",sum(l)/len(l))
# print("La somme :",sum(l))
# print("Le plus grand nombre :",max(l))
# print("Le plus petit nombre :",min(l))
# print("Le nombre total d'élément :",len(l))