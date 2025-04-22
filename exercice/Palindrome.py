def inverser(mot):
    inverse = ""
    for e in mot:
        inverse = e + inverse
    return inverse

mot = input("Entrez un mot : ")
if mot == inverser(mot):
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")