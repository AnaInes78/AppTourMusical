class Review:
    def __init__(self, id, id_evento, id_usuario, calificacion, comentario, animo):
        self.id = id
        self.id_evento = id_evento
        self.id_usuario = id_usuario
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo

    def mostrar_review(self):
        return f"Evento ID: {self.id_evento}, Usuario ID: {self.id_usuario}, Calificación: {self.calificacion}, Comentario: {self.comentario}, Ánimo: {self.animo}"

def cargar_reviews_desde_json(ruta_archivo):
    reviews = []
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
        for review_data in datos:
            review = Review(**review_data)
            reviews.append(review)
    return reviews