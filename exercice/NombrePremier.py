def est_premier(nombre):
    if nombre <= 1:
        return False
    for i in range(2,nombre):
        if nombre % i == 0:
            return False
    return True

nb=int(input("Entrer un nombre :"))
if est_premier(nb):
    print(nb,"est premier")
else:
    print(nb,"n'est pas premier")