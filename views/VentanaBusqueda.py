import tkinter
from tkinter import * 
import tkinter as tk


# Cargar imagen del disco.
#img = tkinter.PhotoImage(file="recital.PNG")

# Insertarla en una etiqueta.
#label = tkinter.Label(ventanaPrin, image=img)
#label.pack()
def print_value():
    value=var.get()
    print(f"El valor ingresado es: {value}")

color_fondo = '#45322e'
white = "white"



 #====FRAMES=====

root=tk.Tk()
root.geometry("600x800")
frame= tk.Frame(root)
frame.pack(fil=tk.BOTH, expand=True)


#====Objetos====

var = tk.StringVar()
entry = tk.Entry(frame, textvariable=var)
entry.pack()



#==== Configuraciones de objetos de login=====

button= tk.Button(frame, text="Imprimir", command=print_value)
button.pack()

root.mainloop()