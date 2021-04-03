#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# contador = 1
# print(contador)
# while contador < 1000:
#     # contador = contador + 1
#     contador += 1
#     print(contador)

# def run():
#     for i in range(1,11):
#         print(" 1 x" ,i , "=", str(1*i))

def run():
    palabra = input("Escriba una Palabra: ")
    for i in palabra:
        print(i.upper())


if __name__ == "__main__":
    run()

