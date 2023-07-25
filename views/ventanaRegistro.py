import tkinter
from tkinter import * 

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
login.place(width=600, height=800,x=0,y=0)



#====Objetos del Registro====

Nombreuser_placeholder = StringVar()
Nombreuser_placeholder.set('Nombre:')

Apellidouser_placeholder = StringVar()
Apellidouser_placeholder.set('Apellido:')

Email_placeholder = StringVar()
Email_placeholder.set('email: ')


password_placeholder = StringVar()
password_placeholder.set('Password')



title = Label(login,text="Registro de Usuarios ")
Nombreuser = Entry(login)
Apellidouser = Entry(login)
Email = Entry(login)
password = Entry(login)

submit = Button(login,text="Crear Usuario")




#==== Configuraciones de objetos de login=====

title.place(x=10,y=10, width=560, height=100)
title.config(font="Roboto 30 normal", fg='white', bg=color_fondo, borderwidth=10)

Nombreuser.place(x=110,y= 150,width=350, height=50)
Nombreuser.config(textvariable=Nombreuser_placeholder, font="Open_Sans 15 normal",
        bg=color_fondo,border=5,fg=white, borderwidth=10)

Apellidouser.place(x=110,y= 250,width=350, height=50)
Apellidouser.config(textvariable=Apellidouser_placeholder, font="Open_Sans 15 normal",
        bg=color_fondo,border=5,fg=white, borderwidth=10)

Email.place(x=110,y= 350,width=350, height=50)
Email.config(textvariable=Email_placeholder, font="Open_Sans 15 normal",
        bg=color_fondo,border=5,fg=white, borderwidth=10)

password.place(x=110,y=450, width=350, height=50)
password.config(textvariable=password_placeholder, font="Open_Sans 15 normal",
            bg=color_fondo, fg="white",bd=10,borderwidth=10)

submit.place(x=140, y=650, width=300,height=40)
submit.config(font="Open_Sans 15 normal",bg="white",fg=color_fondo, borderwidth=10)





main.mainloop()