import tkinter
from tkinter import * 
from PIL import Image, ImageTk

color_fondo = '#45322e'
white = "white"


main = Tk()
main.geometry('600x800')
main.title('App Tours Musical')
main.configure(bg=color_fondo, borderwidth=10)
main.resizable(0,0)
main.configure(highlightbackground="white", borderwidth=10)

 #====FRAMES=====
login = Frame(main, bg="#45322e", borderwidth=10)
login.place(width=580, height=440,x=0,y=0)

# Cargar imagen del disco.
#img = tkinter.PhotoImage(file="C:\Users\Usuario\Desktop\Python\TourMusical\recital.png")
img = ImageTk.PhotoImage(Image.open(f"AppMusical/views/images/{local.recital.png}").resize((200, 200)))
#Insertarla en una etiqueta.
label = tkinter.Label(login, image=img)
label.pack()

#====Objetos del login====

user_placeholder = StringVar()
user_placeholder.set('Nombre  de  usuario')

password_placeholder = StringVar()
password_placeholder.set('Password')

title = Label(login,text="App Tour Musical")
user = Entry(login)
password = Entry(login)

submit = Button(login,text="Iniciar sesion")

registrarse = Button(login,text="Registrarse")

contacto = Button(login,text="Contacto")


#==== Configuraciones de objetos de login=====

title.place(x=10,y=10, width=560, height=100)
title.config(font="Roboto 30 normal", fg='white', bg=color_fondo,borderwidth=10)

user.place(x=110,y= 150,width=350, height=50)
user.config(textvariable=user_placeholder, font="Open_Sans 15 normal",
        bg=color_fondo,border=5,fg=white, borderwidth=10)

password.place(x=110,y=220, width=350, height=50)
password.config(textvariable=password_placeholder, font="Open_Sans 15 normal",
            bg=color_fondo, fg="white",bd=10,borderwidth=10)

submit.place(x=140, y=290, width=300,height=40)
submit.config(font="Open_Sans 15 normal",bg="white",fg=color_fondo, borderwidth=10)

registrarse.place(x=130, y=360, width=150,height=40)
registrarse.config(font="Open_Sans 15 normal",bg="white",fg=color_fondo, borderwidth=10)

contacto.place(x=300, y=360, width=150,height=40)
contacto.config(font="Open_Sans 15 normal",bg=color_fondo,fg='white',borderwidth=10)

main.mainloop()