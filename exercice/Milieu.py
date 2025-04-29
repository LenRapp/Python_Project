def min3(a,b,c):
    if a < b and a < c:
        return a
    elif a > b and b < c:
        return b
    else:
        return c

def max3(a,b,c):
    if b < a and a > c:
        return a
    elif a < b and b > c:
        return b
    else:
        return c

def milieu(a,b,c):
    if a>min3(a,b,c)and a<max3(a,b,c):
        return(a)
    elif b>min3(a,b,c) and b<max3(a,b,c):
        return(b)
    else:
        return(c)

entier=int(input("Entrer un entier : "))
entier2=int(input("Entrer un deuxieme entier : "))
entier3=int(input("Entrer un troisieme entier : "))
print("Le plus petit est",min3(entier,entier2,entier3),
      "Le plus grand est",max3(entier,entier2,entier3),
      "Le milieu est",milieu(entier,entier2,entier3))