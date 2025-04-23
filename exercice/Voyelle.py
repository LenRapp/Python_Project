def nbvoyelle(ch):
    res = 0
    voy="aeiouyAEIOUY"
    for e in ch:
        if e in voy:
            res += 1
    return res

mot = input("Entrez un mot ou phrase : ")
mot2 = input("Entrez un autre mot ou phrase : ")
if nbvoyelle(mot) > nbvoyelle(mot2):
    print("Le mot",mot,"contient plus de voyelle que",mot2)
else:
    print("Le mot",mot2,"contient plus de voyelle que",mot)





