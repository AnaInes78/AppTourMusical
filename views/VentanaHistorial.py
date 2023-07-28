import tkinter
from tkinter import * 

import tkinter as tk
import os
from tkinter import ttk
from PIL import ImageTk, ImageColor, ImageDraw



color_fondo = '#45322e'
white = "white"


main = Tk()
main.geometry('800x1000')
main.title('App Tours Musical')

main.configure(bg=color_fondo, borderwidth=10)
main.resizable(0,0)
main.configure(highlightbackground="white", borderwidth=10)




 #====FRAMES=====
login = Frame(main, bg="#45322e", borderwidth=10)
login.place(width=600, height=800,x=0,y=0)



image =tk.PhotoImage("views/images/recital.png", width=800, height=100)
label = ttk.Label(image=image)
label.pack()


#====Objetos del login====



title = Label(login,text="App Tour Musical\n Historial de Usuario", font="roboto, 12", pady=200)
# mostrar el apellido y nombre del usuario 
#user = print(id_usuario_usuario.json) Apelido y nombre 



volver = Button(login,text="Volver")


#==== Configuraciones de objetos de login=====

title.place(x=10,y=150, width=560, height=100)
title.config(font="Roboto 25 normal", fg='white', bg=color_fondo,borderwidth=10)

# Creamos un Frame para el centro
left_frame = tk.LabelFrame(login, text="Historial de recitales", padx=100, pady=200)
left_frame.pack(side='left', fill='y')


# Entry widget abajo de todo


volver.place(x=300, y=700, width=150,height=40)
volver.config(font="Open_Sans 15 normal",bg=color_fondo,fg='white',borderwidth=10)

main.mainloop()