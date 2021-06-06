import math
import random
import multuply

# def multuply(num1, num2):
#     resultado = num1 * num2
#     return resultado


def run():
    pi = round(math.pi, 3)
    print("# TRYIT: Write a print statement that displays both the type and value of Pi")
    print("EL valor de Pi es",pi)
    print("# TRYIT: Write a conditional to print out if `i` is less than or greater than 50")
    i = random.randint(1,100)
    if i < 50:
        print ("EL valor de 'i' es menor de 50")
    else:
        print("El valor de 'i' es mayor de 50")

    print("# TRYIT: Write a conditional that prints the color of the picked fruit")
    frutaElegida = random.choice(['orange','strawberry','banana'])
    if frutaElegida == 'orange':
        print("La fruta es orange")
    elif frutaElegida == 'strawberry':
        print("La fruta es Roja!")
    elif frutaElegida == 'banana':
        print("La fruta es Amarillo")
    
    print("# TRYIT: Write a function that multiplies two numbers and returns the result")
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    resultado_new = multuply.sendaMultiplicacion(num1, num2)
    print("El Resultado de la Multiplicacion de {} x {} es =".format(num1, num2), resultado_new)
    print("# TRYIT: Write a function that multiplies two numbers and returns the result")
    print("12 x 96 =", multuply.sendaMultiplicacion(12, 96))
    print("48 x 17 =", multuply.sendaMultiplicacion(48, 17))

if __name__ == "__main__":
    run()