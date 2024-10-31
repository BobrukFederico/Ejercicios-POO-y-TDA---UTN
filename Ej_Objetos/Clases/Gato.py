from Clases.Animal import *
class Gato(Animal):
    def __init__(self,nombre):
        super().__init__(nombre)

    def maullar(self):
        print("Miau Miau")