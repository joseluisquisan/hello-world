#!/usr/bin/python3

# Funciones para Modificar el String(Nombre)
# nombre = nombre.capitalize()  # Para poner la primera letra en Mayusculas
# nombre = nombre.upper() # Para poner todo en Mayusc
# nombre = nombre.lower() # Para poner todo en Minusc
# nombre = nombre.strip() # Para quitar espacios en Blanco
# nombre = nombre.replace('a' , 'o') # Reemplaca 'a' por 'o'
# nombre = nombre.strip() # Para quitar espacios en Blanco
# len(nombre) # Para saber cuantos caracteres tiene

def conversor(moneda, dolar):
    pesos = int(input("¿Cuantos pesos " + moneda + " tienes?: "))
    cambio = round((pesos / dolar), 2)
    print("Tienes $", cambio , moneda, sep=" ")

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
        dolar = 720
        conversor("Pesos Chilenos", dolar)
    elif opcion == 2:
        dolar = 720
        conversor("Pesos Argentinos", dolar)
    elif opcion == 3:
        dolar = 2000
        conversor("Bolivares", dolar)
    else:
        print("===== Error, Favor elegir opcion correcta")
        return run()

if __name__ == '__main__':
    run()