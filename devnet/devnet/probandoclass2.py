
class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles"

blue = Car(color="blue" , mileage=20_000)
red = Car(color="red", mileage=30_000)
for car in (blue, red):
    print(car)