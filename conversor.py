#!/usr/bin/python3

def run():
    menu = """
    Conversor de Monedas
    1 - Cambiar monedas Chilenas a Dolares
    2 - Cambiar monedas Argentinas
    """
    print(menu)
    opcion = int(input("Opcion Elegida: "))
    if opcion == 1:
        pesos = int(input("¿Cuantos pesos Chilenos tienes?: "))
        dolar = 716
        cambio = pesos / dolar
        print("Tienes", cambio, "dolares")
    else:
        print("error")


if __name__ == '__main__':
    run()