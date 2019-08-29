def bubble(lista):
    for i in range(len(lista)-1):
        for c in range(len(lista)):
            if lista[i]>lista[i+1]:
             lista[i],lista[i+1],c=lista[i+1],lista[i],c
    print(lista)
    return lista 
