#!/src/bin/python3

import random

def run():
    numero = random.randint(1,10)
    if numero > 5 and numero < 9:
        print("El Numero esta entre 5 y 10")
    elif numero == 9:
        print("El numero es casi 10")
    elif numero == 10:
        print("Es 10!!!!!")
    else:
        print("El Numero es menor a 5")
    print("El numero es", numero)

if __name__ == '__main__':
    run()