import tkinter as tk
from tkinter import ttk, Radiobutton, Checkbutton, Listbox, END, StringVar

# Creamos la ventana principal
root = tk.Tk()
root.title("Ventana con Tkinter")
root.geometry('800x800')

# Creamos un Frame para la barra izquierda
left_frame = tk.LabelFrame(root, text="Barra Izquierda", padx=20, pady=20)
left_frame.pack(side='left', fill='y')


for i in range(3):
    button = tk.Button(left_frame, text=f"Botón {i+1}")
    button.pack(pady=20)

# Listbox en la barra izquierda
modes = ["Dark", "Light"]
mode_listbox = Listbox(left_frame)
for mode in modes:
    mode_listbox.insert(END, mode)
mode_listbox.pack(pady=20)

# Cambiamos la segunda Listbox por un Combobox
scales = ["20%", "40%", "60%", "80%", "100%"]
scale_combobox = ttk.Combobox(left_frame, values=scales)
scale_combobox.pack(pady=20)

# Creamos un Frame para la parte derecha
right_frame = tk.Frame(root)
right_frame.pack(side='right', fill='y')

# Frame para los CheckButtons
checkbutton_frame = tk.LabelFrame(right_frame, text="Grupo de CheckButton")
checkbutton_frame.grid(row=0, column=0, pady=20)

for i in range(3):
    Checkbutton(checkbutton_frame, text=f"CheckButton {i+1}").pack(pady=20)

# Frame para los RadioButtons
radiobutton_frame = tk.LabelFrame(right_frame, text="Grupo de RadioButton")
radiobutton_frame.grid(row=1, column=0, pady=20)

var = StringVar(value="option 1")
for i in range(3):
    Radiobutton(radiobutton_frame, text=f"RadioButton {i+1}", variable=var, value=f"option {i+1}").pack(pady=20)

# Botón a la derecha
right_button = tk.Button(right_frame, text="Derecha")
right_button.grid(row=2, column=0, pady=20)

# Text widget en el centro
text = tk.Text(root, width=40, height=10)
text.insert(tk.END, "Texto sobre tutoriales de Tkinter...")
text.pack(fill='x', padx=20)

# Notebook en el centro
notebook1 = ttk.Notebook(root)
for i in range(3):
    frame = tk.Frame(notebook1)
    label = tk.Label(frame, text=f"Pestaña {i+1}", font=("Arial", 18))
    label.pack(pady=20)
    text = tk.Text(frame, width=30, height=10)
    text.pack(pady=20)
    text.insert(tk.END, f"Contenido de la pestaña {i+1}")
    if i == 0:
        button = tk.Button(frame, text="Button")
    notebook1.add(frame, text=f"Pestaña {i+1}")
notebook1.pack(pady=20)


for i in range(2):
    button = tk.Button(frame, text=f"Botón {i+1}")
    button.pack(pady=20)





# Entry widget abajo de todo
entry = tk.Entry(root)
entry.pack(fill='x', side='bottom', padx=20, pady=20)

root.mainloop()
