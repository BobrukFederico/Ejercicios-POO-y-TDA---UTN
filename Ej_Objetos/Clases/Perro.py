from Clases.Animal import *

class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def ladrar(self):
        print("Guau Guau")