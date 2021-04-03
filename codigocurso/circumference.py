#!/usr/bin/python3

def circumference(radius):
    pi = 3.14
    circumferenceValue = pi * radius * 2
    return circumferenceValue


def run(radius1):
    myCircumference = circumference(radius1)
    print("Circumference of a Circle with radius of " + str(radius) + " is " + str(myCircumference))

radius1 = 2
radius2 = 5
radius3 = 7


if __name__ == '__main__':
    run()