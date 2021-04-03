
def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    if contador == 0:
        return True
    else:
        return False

def run():
    numero = int(input('Escribe el Numero: '))
    if es_primo(numero):
        print('Es Primo!')
    else:
        print('No es primo..')

if __name__ == '__main__':
    run()