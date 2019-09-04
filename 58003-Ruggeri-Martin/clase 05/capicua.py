def palindromo (palabra):
    a=list(palabra.replace(" ",""))
    b=list(palabra.replace(" ",""))
    b.reverse()
    print(palabra)
    print(a)
    print(b)
    if a==b:
        return True
    return False
if __name__=="__main__":
    print(palindromo("agita falsos usos la fatiga"))
