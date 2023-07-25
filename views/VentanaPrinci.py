import tkinter
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


submit = Button(login,text="Indice de Recitales")
Busqueda = Button(login,text="Búsqueda de Recitales ")
Historial = Button(login,text="Historial de Recitales")


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