import tkinter
from tkinter import * 
import customtkinter
from ast import main

import tkinter as tk

import customtkinter
import os
from PIL import Image
import fondolog 
import customtkinter
from PIL import Image
import os

customtkinter.set_appearance_mode("drack")




class App(customtkinter.CTk):
    
    width = 800
    height = 600
    #backgraund="#45322e"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("App Tour Musical Registro")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        #self.configure(bg="#45322e")

        # cargar y crear la imagen de fondo
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(
            Image.open(current_path + "/recital.png"),
            size=(self.width, self.height),
        )
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)


         # crear el frame de login
        #self.backgraund= "#45322e"
        customtkinter.set_default_color_theme("blue") 
        self.login_frame = customtkinter.CTkFrame(self, corner_radius=10, bg_color="#45322e")
        self.login_frame.grid(row=0, column=0, sticky="ns",)
        self.login_label = customtkinter.CTkLabel(
            self.login_frame, 
            text="Bienvenidos App Tour Musical \n Registro de Usuario",
            font=customtkinter.CTkFont("Roboto", size=20, weight="bold"),
        )
        self.login_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(
            self.login_frame, width=200, placeholder_text="Nombre de Usuario"
            
        )
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))

        self.password1_entry = customtkinter.CTkEntry(
            self.login_frame, width=200, show="*", placeholder_text="Contraseña"
        )
        self.password1_entry.grid(row=2, column=0, padx=30, pady=(0, 15))

        
        self.password2_entry = customtkinter.CTkEntry(
            self.login_frame, width=200, show="*", placeholder_text="Confirmar Contraseña"
        )
        self.password2_entry.grid(row=3, column=0, padx=30, pady=(15, 15))
       
        self.login_button = customtkinter.CTkButton(
            self.login_frame, text="Crear Usuario", command=self.login_event, width=200
        )
        self.login_button.grid(row=4, column=0, padx=30, pady=(15, 15))
                 
        # crear el frame principal
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(
            self.main_frame,
            text="Tour Musical\n Registro de Usuarios",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.main_label.grid(row=30, column=0, padx=30, pady=(30, 15))
        self.back_button = customtkinter.CTkButton(
            self.main_frame, text="Volver", command=self.back_event, width=200
        )
        self.back_button.grid(row=6, column=0, padx=30, pady=(15, 15))

    def login_event(self):
        print(
            "Presionó crear usuario ",
            self.login_button.get(open.vista_principal),
                   
        )

        self.login_frame.grid_forget()  # eliminar el frame de login
        self.ventanaOpciones.grid(
            row=0, column=0, sticky="nsew", padx=100
        )  # mostrar el frame principal

    def back_event(self):
        self.vista_principal.grid_forget()  # eliminar el frame principal
        self.login_frame.grid(row=0, column=0, sticky="ns")  # mostrar el frame de login

if __name__ == "__main__":
    app = App()
    app.mainloop()