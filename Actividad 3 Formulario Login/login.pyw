import tkinter as tk
from PIL import Image, ImageTk

login = tk.Tk()
path = Image.open("imagen-login-logo.jpg")
icono = ImageTk.PhotoImage(path)
login.iconphoto(True, icono)
login.geometry('800x500')

login.resizable(False,False)

login.title('CYBERCODE PROGRAMING')

frame = tk.Frame(login, width=350, height=800,relief="raised",bd=1,bg="cyan3" )
frame.grid(row=0,column=0,pady=0)

imagen = Image.open("imagen-login.jpg")
imagen = imagen.resize((260,260))
imagen = ImageTk.PhotoImage(imagen)
label = tk.Label(frame, image = imagen)
label.image = imagen
label.pack()
label.place(relx = 0.5, rely=0.3,anchor="center")

etiquetalogin= tk.Label(login, text="LOGIN", bg="cyan3", fg="white", font=("Times New Roman", 16), width = 20, height = 2, anchor= "center")
etiquetalogin.grid(row = 0,column = 2, pady= 0,sticky="n")



login.mainloop()    