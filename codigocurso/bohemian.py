# def run():
#     for i in range(6):
#         if i == 3:
#             print("Figarooo")
#             continue
#         print("Galileo")

def run():
    for contador in range(101):
        if contador % 2 != 0:
            print("Impar")
            continue
        print("Par ", contador, "")

if __name__ == '__main__':
    run()