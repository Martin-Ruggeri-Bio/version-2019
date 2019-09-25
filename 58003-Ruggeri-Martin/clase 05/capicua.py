def palindromo (palabra):
    b=list(palabra.replace(" ",""))
    b.reverse()
    print(b)
    return list(palabra.replace(" ",""))==b
if __name__=="__main__":
    print("ingrese frase")
    palabra=input()
    print(palindromo(palabra))
