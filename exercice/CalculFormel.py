def somme(ch):
    a=int(ch[0])
    b=int(ch[2])
    c=int(ch[4])
    d=int(ch[6])
    return ([a*d+b*c,b*d])


def p(a,b):
    if b == 0:
        return a
    else:
        return p(b,a%b)

def fractionsimp(a,b):
    num = a//p(a,b)
    den = b//p(a,b)
    return(str(num)+"/"+str(den))

#programme principal

ch=str(input("Entrer une somme de faction type 'a/b+c/d' :"))
print("La fonction simplifiée est "+ fractionsimp(somme(ch)[0], somme(ch)[1]))
