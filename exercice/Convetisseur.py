def celsuisVersFahrenheit(c):
    f =  (c * 9 / 5 + 32)
    return f
def fahrenheitVersCelsuis(f):
    c = (f - 32) * 5 / 9
    return c

def demanderConvertion():
    print("1 - Convertir Celsius vers Fahrenheit")
    print("2 - Convertir Fahrenheit vers Celsius")
    choix = int(input("1 ou 2 : "))
    return choix


choix = demanderConvertion()
if choix == 1:
    celsuis = float(input("Entrez la valeur en Celsius : "))
    res = celsuisVersFahrenheit(celsuis)
    print("Résultat :", res, "°F")
elif choix == 2:
    fahrenheit = float(input("Entrez la valeur en Fahrenheit : "))
    res = fahrenheitVersCelsuis(fahrenheit)
    print("Résultat :", res, "°C")
else :
    print("Veuillez choisir une option valide")
