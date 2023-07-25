from views.vista_principal import VistaPrincipal
from models.recital import Recital
from models.ubicacion import Ubicacion
from PIL import Image, ImageTk

class ControladorPrincipal:
    def __init__(self, root):
        self.vista = VistaPrincipal(root, self.seleccionar_recital, seleccionar_ubicacion)
        self.recitales = Recital.cargar_recitales("AppTourMusical/data/recitales.json")
        self.ubicaciones = Ubicacion.cargar_ubicaciones("AppTourMusical/data/ubicaciones.json")
        self.marcadores = []
        self.imagenes = []

        self.cargar_recitales()
        self.cargar_imagenes()
        self.cargar_marcadores()
        
    def cargar_recitales(self):
        for recital in self.recitales:
            self.vista.agregar_recital(recital)
        
    def cargar_imagenes(self):
        for recital in self.recitales:
            imagen = ImageTk.PhotoImage(Image.open(f"AppToursMusical/views/images/{recital.imagen}").resize((00, 200)))
            self.imagenes.append(imagen)

    def cargar_marcadores(self):
        for ubicacion, recital in zip(self.ubicaciones, self.recitales):
            imagen = self.imagenes[ubicacion.id - 1]
            marcador = self.vista.agregar_marcador_mapa(ubicacion.latitud, ubicacion.longitud, recital.nombre, imagen)
            marcador.hide_image(True)
            self.marcadores.append(marcador)

    def seleccionar_recital(self, event):
        # Obtiene el índice del elemento seleccionado
        indice_seleccionado = self.vista.lista_recitales.curselection()
        # Obtiene el local seleccionado
        local_seleccionado = self.recitales[indice_seleccionado[0]]
        
        ubicacion_seleccionada = Ubicacion(0, 0, 0, "")
        
        # Busca la ubicación correspondiente al recital seleccionado
        for ubicacion in self.ubicaciones:
            if ubicacion.id == recital_seleccionado.id_ubicacion:
                ubicacion_seleccionada = ubicacion
                break
        
        # Centra el mapa en la ubicación seleccionada
        self.vista.mapa.set_position(ubicacion_seleccionada.latitud, ubicacion_seleccionada.longitud)

        print(f"Latitud: {ubicacion_seleccionada.latitud}, Longitud: {ubicacion_seleccionada.longitud}")

def seleccionar_ubicacion(marcador):
    if marcador.image_hidden is True:
        marcador.hide_image(False)
    else:
        marcador.hide_image(True)
    print("Ubicación seleccionada: ", marcador.text)