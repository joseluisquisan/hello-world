#!/usr/bin/python3
import random

def run():
    vidas = 3
    numero_aleatorio = random.randint(1 , 10)
    print('Hola, Tienes ' + str(vidas) + ' vidas')
    numero_elegido = int(input('Elige un numero del 1 al 10: '))
    while vidas >= 1:
        if numero_elegido < numero_aleatorio:
            vidas -= 1
            print('Elige un numero más grande')
        elif numero_elegido > numero_aleatorio:
            vidas -= 1
            print('Elige un numero más pequeño')
        elif numero_elegido == numero_aleatorio:
            print('Bingo! has ganado!')
            break
        print('Ups!, te quedan ' + str(vidas) + ' vidas!')
        print(numero_aleatorio)
        numero_elegido = int(input('Elige un numero del 1 al 10: '))


if __name__ == '__main__':
    run()