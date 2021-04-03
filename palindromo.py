#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabraINV = palabra[::-1]
    if palabra == palabraINV:
        return True
    else: 
        return False



def run():
    palabra = input('Cual es tu Palabra/Frase?: ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('Es Palindromo')
    else:
        print('NO es Palindromo')


if __name__ == '__main__':
    run()