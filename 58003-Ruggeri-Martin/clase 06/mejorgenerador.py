import random
def mejor_generador( minimo,maximo,lista):
    encontrado = True
    while encontrado:
        aleatorio = random.randint(minimo,maximo)
        encontrado = aleatorio in lista
    return aleatorio
print(mejor_generador(3,4,[3]))
