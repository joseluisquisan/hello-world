#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# Funciones para Modificar el String(Nombre)
# nombre = nombre.capitalize()  # Para poner la primera letra en Mayusculas
# nombre = nombre.upper() # Para poner todo en Mayusc
# nombre = nombre.lower() # Para poner todo en Minusc
# nombre = nombre.strip() # Para quitar espacios en Blanco
# nombre = nombre.replace('a' , 'o') # Reemplaca 'a' por 'o'
# nombre = nombre.strip() # Para quitar espacios en Blanco

# len(nombre) # Para saber cuantos caracteres tiene

def conversor(tipo_pesos, valor_dolar):
    pesos = input('Cuantos ' + tipo_pesos + ' Tienes? ')
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print('Tienes $' + dolares + ' USD 💲')

nombre = input('Hola Amigazo!, Cual es tu nombre? ')
nombre = nombre.capitalize()

menu = """ 
Bienvenido """ + nombre +  """ al sistema de conversion de Monedas 🎩
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Bolivares Venezolanos
Elige porfavor una opción : """

# Atajo para sacar las triples Comillas: Shift + Alt + A

opcion = int(input(menu))

if opcion == 1:
    conversor("Pesos Colombianos", 3875)
elif opcion == 2:
    conversor("Pesos Argentinos", 65)
elif opcion == 3:
    conversor("Bolivares Venezolanos", 2000000)
else:
    print('Ingresa por favor una opción correcta')
    print('')
    opcion = int(input(menu))
