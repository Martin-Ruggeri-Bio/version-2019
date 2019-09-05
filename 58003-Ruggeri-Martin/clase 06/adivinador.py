from generador import generador
adivinado=False
aleatorio=generador(1,20)
while adivinado == False:
    print("ingrese un numero entre 1 y 20")
    numero=int(input())
    if numero==aleatorio:
        print("adivinaste!!!")
        adivinado=True
    if numero<aleatorio:
        print("salame ingrea un numero mas grande")
    if numero>aleatorio:
        print("nabo,es mas chico")