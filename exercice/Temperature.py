temp=(int(input("Entrer une température : ")))
if temp <= 0:
    print("C'est de la glace")
elif 0 < temp < 100:
    print("C'est de l'eau liquide")
else:
    print("C'est de la vapeur")
