#!/usr/bin/python3

def run():
    limite = int(input('Hasta donde quiere que elevemos? : '))
    elevacion = 0
    while elevacion < limite:
        print('La potencia de 2 elevado a la ', elevacion, 'es igual', 2**elevacion)
        elevacion = elevacion + 1

if __name__ == '__main__':
    run()