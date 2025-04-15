import random
def menu():
    print("Bienvenue sur Devine le nombre !")
    print("1: Jouer")
    print("2: Exit")

def jouer():
    nbAlea =random.randint(1,100)
    essaie =0
    print ("🤖 J'ai choisis un nombre entre 1 et 100")
    print(nbAlea)

    while True:
        nbUser=int(input("Votre proposition : "))
        essaie +=1


        if nbUser < nbAlea:
            print("Votre nombre est trop petit !")
        elif nbUser > nbAlea:
            print("Votre nombre est trop grand !")
        else:
            print("Bravo !!! Vous avez gagner le nombre était", nbAlea, "en ",essaie, "essaie")
            break


def main():
    while True:
        menu()
        choix = int(input("Choisis une option : "))

        if choix == 1:
            jouer()
        elif choix == 2:
            print("Merci d'avoir jouer")
            break


        rejouer = input("Rejouer (o/n) : ").lower()
        if rejouer != 'o':
            print("Merci d'avoir jouer")
            break

if __name__ == '__main__':
    main()


