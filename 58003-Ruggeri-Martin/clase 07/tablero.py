def full(tablero):
    return not " " in tablero
def draw_tablero(tablero):
    print(" "+tablero[0]+" | "+tablero[1]+" | "+tablero[2])
    print("---+---+---")
    print(" "+tablero[3]+" | "+tablero[4]+" | "+tablero[5])
    print("---+---+---")
    print(" "+tablero[6]+" | "+tablero[7]+" | "+tablero[8])
def validate(tablero, posicion):
    return tablero[posicion -1]==" "
def win(tablero):
    if tablero[0]!=" " and tablero[0]==tablero[4] and tablero [4]==tablero[8]:
        return True
    if tablero[2]!=" " and tablero[2]==tablero[4] and tablero [4]==tablero[6]:
        return True
    for i in range (0,3):
        if tablero[i]!=" " and tablero[i]==tablero[i+3] and tablero[i]==tablero[i+6]:
            return True
    for i in range (0,7,3):
        if tablero[i]!=" " and tablero[i]==tablero[i+1] and tablero[i]==tablero[i+2]:
            return True
    return False
            