print("Les tables de multiplications")
n=int(input("Entrer un nombre : "))
jusqua=int(input("Jusqu'à: "))

for i in range(1, jusqua + 1):
    print(i,"*",n, "=", i * n)