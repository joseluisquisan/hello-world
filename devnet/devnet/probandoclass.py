#Class, una estructura de datos, un arreglo para los objeto
#Class, tiene funciones (def) llamadas) *Metodos*
#Instance, es un Objeto creado desde la Class
#Atributos creados dentro del __init__ , son Atributos iniciales de las Instances
#Atributos Comunes (Class Atributes). se crean fuera del __init__
#Instance Methods,(Metodos, (def)), definidas dentro de la clases y solo pueden ser llamadas por las Instancias

class Dog:
    #Class Atribute, un Atributo para
    species = "Canino"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.breed = breed
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
# class JackRussellTerrier(Dog):
#     pass

# class Dachshund(Dog):
#     pass

# class Bulldog(Dog):
#     pass

miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")