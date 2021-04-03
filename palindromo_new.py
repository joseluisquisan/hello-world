#!/usr/bin/python3

def run():
    frase = input("Amigo, escribe una palabra: ")
    frase = frase.lower()
    frase = frase.replace(" ", "")
    print(frase)
    frase_inversa = frase[::-1]
    if frase == frase_inversa:
        print("Es un Palindromo!")
    else:
        print("no es un palindromo :(")

if __name__ == '__main__':
    run()