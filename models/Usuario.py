class Usuario:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.historial_eventos = []

    def agregar_evento_historial(self, id_evento):
        self.historial_eventos.append(id_evento)

    def obtener_historial_eventos(self):
        return self.historial_eventos

def cargar_usuarios_desde_json(ruta_archivo):
    usuarios = []
    with open(ruta_archivo, 'r') as archivo:
        datos = json.load(archivo)
        for usuario_data in datos:
            usuario = Usuario(**usuario_data)
            usuarios.append(usuario)
    return usuarios
