#!/src/bin/python3

import math
import random

def multiply(num1, num2):
    result = num1 * num2
    return result


def run():
# TRYIT: Write a print statement that displays both the type and value of Pi
    pi = math.pi
    print("====== 1er Desafio ======")
    print("El parametro Pi es de tipo {} y el valor es de {}".format(type(math.pi), pi))
# TRYIT: Write a conditional to print out if `i` is less than or greater than 50
    print("====== 2er Desafio ======")
    i = random.randint(1,10)
    if i < 5:
        print("i es menor a 5")
    elif i == 5:
        print("i es igual a 5")
    else:
        print("i es mayor a 5")
# TRYIT: Write a conditional that prints the color of the picked fruit
    print("====== 3er Desafio ======")
    picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
    if picked_fruit == 'orange':
        print("The fruit is orange")
    elif picked_fruit == 'strawberry':
        print("The fruit is red")
    elif picked_fruit == 'banana':
        print("The fruit is yellow")
# TRYIT: Write a function that multiplies two numbers and returns the result
    print("====== 4er Desafio ======")
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    resultado_nuevo = multiply(a, b)
    print("Multiplicar",a , "x",b , " es igual a =", resultado_nuevo)
# TRYIT: Now call the function a few times to calculate the following answers
    print("Multiplicar",a , "x",b , " es igual a =", resultado_nuevo)



if __name__ == '__main__':
    run()
