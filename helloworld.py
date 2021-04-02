#!/usr/bin/python3

def run():
    menu = """
    Conversor de Monedas
    1 - Cambiar monedas Chilenas
    2 - Cambiar monedas Argentinas
    """
    print(menu)
    opcion = input("Opcion Elegida: ")

    if opcion == 1:
        print("Son Chilenos")
    else:
        print("son argentinos")

if __name__ == '__main__':
    run()