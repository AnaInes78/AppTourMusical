import tkinter as tk
from tkinter import *

color_fondo = '#45322e'
white = "white"


main = Tk()
main.geometry('600x800')
main.title('App Tours Musical- Bienvenido')
main.configure(bg=color_fondo, borderwidth=10)
main.resizable(0,0)
main.configure(highlightbackground="white", borderwidth=10)

 #====FRAMES=====
login = Frame(main, bg="#45322e", borderwidth=10)
login.place(width=600, height=800,x=0,y=0)



#====Objetos ====


title = Label(login,text="Bienvenido/a")
#... enlaces ..#
def abrir_ventana_indice_recitales():
    main.withdraw()  # Ocultar la ventana de inicio
    ventana_indice_recitales = tk.Toplevel(main)
    VentanaIndiceRecitales(ventana_indice_recitales)
class VentanaIndiceRecitales:
    def __init__(self, root):
        self.root = root
        self.root.title("Índice de Recitales")
        # Aquí puedes agregar elementos y funcionalidades para mostrar el índice de recitales

# ...

class VentanaBusquedaRecitales:
    def __init__(self, root):
        self.root = root
        self.root.title("Búsqueda de Recitales")
        # Aquí puedes agregar elementos y funcionalidades para realizar la búsqueda de recitales

# ...

def abrir_ventana_busqueda_recitales():
    main.withdraw()  # Ocultar la ventana de inicio
    ventana_busqueda_recitales = tk.Toplevel(main)
    VentanaBusquedaRecitales(ventana_busqueda_recitales)

class VentanaHistorialRecitales:
    def __init__(self, root):
        self.root = root
        self.root.title("Historial de Recitales")
        # Aquí puedes agregar elementos y funcionalidades para mostrar el historial de recitales

# ...

def abrir_ventana_historial_recitales():
    main.withdraw()  # Ocultar la ventana de inicio
    ventana_historial_recitales = tk.Toplevel(main)
    VentanaHistorialRecitales(ventana_historial_recitales)


submit = Button(login,text="Indice de Recitales", command=abrir_ventana_indice_recitales)
Busqueda = Button(login,text="Búsqueda de Recitales ",command=abrir_ventana_busqueda_recitales)
Historial = Button(login,text="Historial de Recitales",command=abrir_ventana_historial_recitales)


#==== Configuraciones de objetos de login=====


title.place(x=10,y=10, width=560, height=100)
title.config(font="Roboto 30 normal", fg='white', bg=color_fondo,borderwidth=10)

submit.place(x=140, y=260, width=350,height=40)
submit.config(font="Open_Sans 15 normal",bg="white",fg=color_fondo, borderwidth=10)

Busqueda.place(x=130, y=360, width=350,height=40)
Busqueda.config(font="Open_Sans 15 normal",bg="white",fg=color_fondo, borderwidth=10)

Historial.place(x=130, y=460, width=350,height=40)
Historial.config(font="Open_Sans 15 normal",bg="white",fg=color_fondo, borderwidth=10)

main.mainloop()