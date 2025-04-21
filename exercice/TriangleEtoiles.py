nbEtoile=int(input("Combien de lignes : "))
for i in range(nbEtoile):
    print(" "*(nbEtoile-i-1)+"*"*(2*i+1))