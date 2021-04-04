#!/usr/bin/python3

# def run():
#     for i in range(100):
#         if i % 2 != 0:
#             continue
#         print(i)

# def run():
#     for i in range(1000000):
#         print(i)
#         if i == 567888:
#             break

def run():
    texto = input('Escribe algo: ')
    for i in texto:
        print(i)
        if i == 'o':
            break


if __name__ == '__main__':
    run()