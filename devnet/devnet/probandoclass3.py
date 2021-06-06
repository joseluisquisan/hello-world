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
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} barks: {sound}"
    
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf!"):
        return super().speak(sound)
        # return f"Oh! Mami Look!.. {self.name}'ve said {sound}"

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

class GoldenRetreiver(Dog):
    def speak(self, sound="BArk!")
    return super().speak(sound)

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)