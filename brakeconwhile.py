

def run():
    print("Adivina que Edad Tengo ")
    intentos = 0
    while intentos < 3:
        edad = int(input("¿Que Edad Tengo?: "))
        if edad == 33:
            print("Acertaste!")
            break
        else:
            intentos += 1
            print("Fallaste :(")

if __name__ == '__main__':
    run()