#!/usr/bin/python3

def run(potencia_inicial, resultado):
    if resultado <=1000000:
        resultado = (2**potencia_inicial)
        # print(resultado)
        print('2 Elevado a ' + str(potencia_inicial) + ' es igual a: ' + str(resultado))
        potencia_inicial = potencia_inicial + 1
        run(potencia_inicial, resultado)
    else:
        print('Fin!')

if __name__ == '__main__':
    potencia_inicial = 0
    resultado = 0
    run(potencia_inicial, resultado)