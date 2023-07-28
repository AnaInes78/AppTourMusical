import tkinter as tk




from controller.controlador_principal import ControladorPrincipal

root = tk.Tk()
root.title("Próximos Recitales en Argentina ")

controlador=ControladorPrincipal(root)



root.mainloop()