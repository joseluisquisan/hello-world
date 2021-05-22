def run():
    my_list =[1, 2, 3, 4, 5]

    # new_list = [i**2 for i in my_list]

    # print(new_list)

    new_list = []

    for i in my_list:
        new_list.append(i**2)
    
    print(new_list)

if __name__ == '__main__':
    run()