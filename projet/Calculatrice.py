def addition(a,b):
    return a+b

def soustraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b == 0:
        return "Erreur: division par zero"
    return a/b

def puissance(a,b):
    return a**b

def menu():
    print("=== CALCULATRICE ===")
    print("Entrer votre choix")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Puissance")
    print("0.Exit")

def main():
    while True:
        menu()
        choix = int(input("Entrer votre choix: "))

        if choix == 0:
            print("Fin de la CALCULATRICE")
            break

        if choix < 0 or choix > 5:
            print("Veulliez choisir un choix entre 0 et 5")
            continue


        a=float(input("Entrer un nombre: "))
        b=float(input("Entrer un deuxieme nombre: "))


        if choix == 1:
            print("Reésultat :", addition(a,b))
            continue
        elif choix == 2:
            print("Résultat :", soustraction(a,b))
        elif choix == 3:
            print("Résultat :", multiplication(a,b))
        elif choix == 4:
            print("Résultat :", division(a,b))
        elif choix == 5:
            print("Résultat :", puissance(a,b))

        continuer = input("Faire un autre calcul ? (y/n)")
        # .lower transforme les caracteres en minuscule
        if continuer.lower() != 'y':
            print("Fin de la CALCULATRICE")
            break

if __name__ == '__main__':
    main()

