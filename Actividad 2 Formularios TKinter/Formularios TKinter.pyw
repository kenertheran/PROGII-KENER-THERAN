import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
def registrar():
    
    mensaje = f"Nombre: {cnombre.get()}\nApellido: {capellido.get()}\nEdad: {cedad.get()}\nDirección: {cdireccion.get()}\nGenero: {genero.get()}\ncelular4: {ccelular.get()}\nCiudad: {selecciona_ciudad.get()}"
    messagebox.showinfo("Datos registrados", mensaje)
    
ventana=tk.Tk()

path = Image.open("Logo-Tecnar.png")
icono = ImageTk.PhotoImage(path)
ventana.iconphoto(True, icono)

ventana.title("Tecnar App")
ventana.geometry("800x800")
ventana.resizable(True,True)
ventana.config(bg="deep sky blue")

Lnombre=tk.Label(ventana,text="nombre: " )
Lnombre.grid(row = 0, column = 25, pady = 4)
cnombre=tk.Entry(ventana, width = 30)
cnombre.grid(row = 1, column = 25, pady = 4)

Lapellido=tk.Label(ventana,text="apellido: " )
Lapellido.grid(row = 3, column = 25, pady = 4)
capellido=tk.Entry(ventana, width = 30)
capellido.grid(row = 4, column = 25, pady = 4)

Ledad=tk.Label(ventana,text="edad: " )
Ledad.grid(row = 5, column = 25, pady = 4)
cedad=tk.Entry(ventana, width=30)
cedad.grid(row = 6, column = 25, pady = 4)

Ldireccion=tk.Label(ventana,text="direccion: " )
Ldireccion.grid(row = 7, column = 25, pady = 4)
cdireccion=tk.Entry(ventana, width = 30)
cdireccion.grid(row = 8, column = 25, pady = 4)

Lgenero=tk.Label(ventana,text="genero: " )
Lgenero.grid(row = 9, column = 25, pady = 4)
genero = tk.StringVar()

tk.Radiobutton(ventana, text="Masculino", variable=genero, value="Masculino").grid(row=10, column=25, pady=4)
tk.Radiobutton(ventana, text="Femenino", variable=genero, value="Femenino").grid(row=11, column=25, pady=4)

Lcelular=tk.Label(ventana,text="celular: " )
Lcelular.grid(row = 12, column = 25, pady = 4)
ccelular=tk.Entry(ventana, width = 30)
ccelular.grid(row = 13, column = 25, pady = 4)

lciudad=tk.Label(ventana,text="Ciudad:")
lciudad.grid(row = 14, column = 25, pady = 4)
selecciona_ciudad = tk.StringVar()

ciudades = ["Cartagena", "Barranquilla", "Bogota", "Medellin", "Cali"]

lista_ciudad= tk.Listbox(ventana, height=5)
lista_ciudad.grid(row = 15, column = 25, pady = 4)
for ciudad in ciudades:
    lista_ciudad.insert(tk.END, ciudad)


def on_select(event):
    selecciona_ciudad.set(event.widget.get(event.widget.curselection()))

lista_ciudad.bind('<<ListboxSelect>>', on_select)

Registrar = tk.Button(ventana, text = "Registrar",bg="cyan", command=registrar)

Registrar.grid(row = 16, column = 1, pady = 4)

ventana.mainloop()