class Libro:
    def __init__(self, id: int ,titulo: str, autor: str, año_publicacion: int):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año_publicacion = año_publicacion
    

    def retornar_descripcion(self):
        print(f"El id del libro es: {self.id}, el titulo es: {self.titulo}, su autor: {self.autor} y su año de publicacion: {self.año_publicacion}")