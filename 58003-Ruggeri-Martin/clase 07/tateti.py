from tablero import draw_tablero,full,validate,win
tablero=[]
for i in range(0,9):
    tablero.append(" ")
    #posicion=int(input())(es el scan)
draw_tablero(tablero)
while win(tablero)==False and full(tablero)==False:
    print("turno x")
    valido=False
    while not valido:
        print("ingresa un posicion del 1 al 9 (X):")
        posicion=int(input())
        valido=validate(tablero,posicion)
        if not valido:
            print("error de posicion")
    tablero[posicion-1]="x"
    draw_tablero(tablero)
    gano=win(tablero)
    if gano:
        print("gano (X)")
    else:
        print("turno O")
        valido=False
        while not valido:
            print("ingresa un posicion del 1 al 9 (O):")
            posicion=int(input())
            valido=validate(tablero,posicion)
            if not valido:
                print("error de posicion")
        tablero[posicion-1]="O"
        draw_tablero(tablero)
        gano=win(tablero)
        if gano:
            print("gano (O)")
if full(tablero) and not win(tablero):
    print("Nadie gano")