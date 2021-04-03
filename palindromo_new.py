#!/usr/bin/python3


def es_palindromo(frase):
    frase = frase.lower()
    frase = frase.replace(" ", "")
    frase_inversa = frase[::-1]
    if frase == frase_inversa:
        return True
    else:
        return False
    

def run():
    palabra = input("Amigo, escribe una palabra: ")
    mi_palindromo = es_palindromo(palabra)
    if mi_palindromo == True:
        print("Es Palindromo")
    elif mi_palindromo == False:
        print("No lo es")


if __name__ == '__main__':
    run()