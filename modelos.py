class Artista:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento, fecha_muerte):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

class ObraDeArte:
    def __init__(self, id_objeto, titulo, clasificacion, fecha_objeto, artista, url_imagen):
        self.id_objeto = id_objeto
        self.titulo = titulo
        self.clasificacion = clasificacion
        self.fecha_objeto = fecha_objeto
        self.artista = artista
        self.url_imagen = url_imagen