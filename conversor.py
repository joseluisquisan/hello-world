#!/usr/bin/python3

def conversor(pesos, dolar):
    cambio = round((pesos / dolar), 2)
    print("Tienes $", cambio, "dolares")

def run():
    menu = """
    Conversor de Monedas
    1 - Cambiar monedas Chilenas a Dolares
    2 - Cambiar monedas Argentinas a Dolares
    3 - Cambiar monedas Venezolanas a Dolares
    """
    print(menu)
    opcion = int(input("Opcion Elegida: "))
    if opcion == 1:
        pesos = int(input("¿Cuantos pesos Chilenos tienes?: "))
        dolar = 720
        conversor(pesos, dolar)
    elif opcion == 2:
        pesos = int(input("¿Cuantos pesos Argentinos tienes?: "))
        dolar = 7000
        conversor(pesos, dolar)
    elif opcion == 3:
        pesos = int(input("¿Cuantos Bolivares tienes?: "))
        dolar = 2000
        conversor(pesos, dolar)
    else:
        print("===== Error, Favor elegir opcion correcta")

if __name__ == '__main__':
    run()