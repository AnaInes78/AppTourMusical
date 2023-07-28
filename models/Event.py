class Event:
    def __init__(self, id, nombre, artista, genero, id_ubicacion, hora_inicio, hora_fin, descripcion, imagen):
        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.genero = genero
        self.id_ubicacion = id_ubicacion
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin
        self.descripcion = descripcion
        self.imagen = imagen

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'artista': self.artista,
            'genero': self.genero,
            'id_ubicacion': self.id_ubicacion,
            'hora_inicio': self.hora_inicio,
            'hora_fin': self.hora_fin,
            'descripcion': self.descripcion,
            'imagen': self.imagen
        }
#importar datos
import json

def cargar_eventos_desde_json(ruta_archivo):
    eventos = []
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
        for evento_data in datos:
            evento = Event(**evento_data)
            eventos.append(evento)
    return eventos
