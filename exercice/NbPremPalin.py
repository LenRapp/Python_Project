def est_premier(nombre):
    for i in range(2,nombre):
        if nombre % i == 0:
            return False
    return True


def sommeChiffres(nb):
    somme = 0
    ch = str(nb)
    for e in ch:
        somme += int(e)
    return somme

def change(n):
    nb = str(n)
    ch=""
    for e in nb:
        ch = e + ch
    res = int(ch)
    return res

#Programme principal

nb = 10000
while not (est_premier(nb) and sommeChiffres(nb) == 19 and  change(nb) == nb):
    nb += 1
print("Le nombre est", nb)
