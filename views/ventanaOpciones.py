import tkinter
import tkinter as tk
from tkinter import ttk, Radiobutton, Checkbutton, Listbox, END, StringVar
from tkinter import *
from typing import Self 
import customtkinter
import os
from PIL import Image

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
login.place(width=800, height=800,x=0,y=0)
title = Label(login,text="Bienvenido/a")


# Creamos un Frame para la barra izquierda
left_frame = tk.LabelFrame(login, text="Barra Izquierda", padx=20, pady=20)
left_frame.pack(side='left', fill='y')

submit = Button(login,text="Indice de Recitales")
Busqueda = Button(login,text="Búsqueda de Recitales ",fg="blue", command=Busqueda)
Historial = Button(login,text="Historial de Recitales")

# Creamos un Frame para la parte derecha
right_frame = tk.Frame(login)
right_frame.pack(side='right', fill='y')

#====Objetos ====





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