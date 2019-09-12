from generador import generador
buscado=generador(1,10000)
min=1
max=10000
adivinado=False
while adivinado==False:
    print ("ingresa un numero")
    numero=int(input())
    if numero==buscado:
        adivinado=True
        print("ganaste")
    if numero<buscado:
        print("el numero es mayor")
    if numero>buscado:
        print("el numero es menor")
    if adivinado==False:
        print("le toca a la pc")
        numero=generador(min,max)
        if numero==buscado:
            adivinado=True
            print("la pc gano, y eligio "+str(numero))
        if numero<buscado:
            print("la pc eligio que es menor y es "+str(numero))
            min=numero
        if numero>buscado:
            print("la pc eligio que es mayor y es "+str(numero))
            max=numero
        

