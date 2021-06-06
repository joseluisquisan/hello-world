#!/usr/bin/python3

def run():
    i_am_hungry = False
    nombre="Jose Luis"
    apellido="Quintero Sanchez"
    fullName = nombre
    fullName += " "
    fullName += apellido
    if i_am_hungry:
        print("Feed me man!!")
    else:
        print("Im OK baby")
        print("Hola, mi nombre es {nombre1} {apellido1}".format(nombre1=nombre, apellido1=apellido))
        print("Mi nombre tiene", len(nombre), "caracteres")
        print("PRobanco mi nombre completo",fullName)

if __name__ == '__main__':
    run()