def circumference(radius):
    pi = 3.14
    circumferenceValue = pi * radius * 2
    return circumferenceValue
    
def printCircumference(radius):
    myCircumference = circumference(radius)
    print("Circumference of a Circle with a Radius of " + str(radius) + " is " + str(myCircumference))
