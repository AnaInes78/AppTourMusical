import tkinter as tk
from tkinter import ttk


root= tk.Tk()
root.title("App Tour Musical")

frame=ttk.Frame(root).grid()

root.configure(background="#45322e")
root.configure(highlightbackground="#A1A892", border=10)
#root.pack_slaves(width=580, height=440,x=0,y=0)




label1=tk.Label(root, text="Bienvenidos a tu App Tour Musical")
label1.grid(row=0, column=0, columnspan=2)



label2=tk.Label(root, text="Ingresa haz clic en Iniciar Sesión para loguearte: ")
label2.grid(row=3, column=0)

ttk.Button(frame, text="Iniciar Sesion", command=lambda: print("inicio sesión")).grid()

label3=tk.Label(root, text="Si eres nuevo, haz clic en registrate ")
label3.grid(row=6, column=0)

ttk.Button(frame, text="Registrarte", command=lambda: print("Registarse")).grid()
root.mainloop()

