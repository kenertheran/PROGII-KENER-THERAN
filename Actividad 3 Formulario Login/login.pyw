import tkinter as tk
from PIL import Image, ImageTk

login = tk.Tk()
path = Image.open("imagen-login-logo.jpg")
icono = ImageTk.PhotoImage(path)
login.iconphoto(True, icono)
login.geometry('800x500')

login.resizable(False,False)

login.title('CYBERCODE PROGRAMING')

frame = tk.Frame(login, width=300, height=800,relief="raised",bd=1,bg="cyan3" )
frame.grid(row=0,column=0,pady=0)

imagen = Image.open("imagen-login.jpg")
imagen = imagen.resize((260,260))
imagen = ImageTk.PhotoImage(imagen)
label = tk.Label(frame, image = imagen)
label.image = imagen
label.pack()
label.place(relx = 0.5, rely=0.3,anchor="center")

frame1 = tk.Frame(login, width=200, height=300, relief="raised",bd=2,bg= "cyan3")
frame1.grid(row=0, column=1,pady= 10,padx=10)

def contenido_login():
    frame1.update_idletasks()
    width = frame1.winfo_width()
    height = frame1.winfo_height()
    x = (frame1.winfo_toplevel().winfo_width() - width) / 2
    y = (frame1.winfo_toplevel().winfo_height() - height) / 2
    frame1.place(in_=login, relx=0.65, rely=0.6, x=-width/2, y=-height/2)
    
    
contenido_login()

etiquetalogin= tk.Label(login, text="LOGIN", bg="cyan3", fg="black",bd= 5, font=("Times New Roman", 16), width = 20, height = 2, anchor= "center")
etiquetalogin.grid(row = 0,column = 10, padx=120, pady=(10, 10),sticky="n")

usuario_label = tk.Label(frame1, text="Usuario:",font=("Times New Roman",12), bg="deep sky blue")
usuario_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

usuario_entry = tk.Entry(frame1)
usuario_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

contrasena_label = tk.Label(frame1, text="Contraseña:",font=("Times New Roman",12), bg="deep sky blue")
contrasena_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

contrasena_entry = tk.Entry(frame1, show="*")
contrasena_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

login_button = tk.Button(frame1, text="Iniciar sesión", bg="medium spring green", fg="black", font=("Times New Roman", 12))
login_button.grid(row=3, column=0, columnspan=2, pady=10)

registro_button = tk.Button(frame1, text="Registrarse", bg="deep sky blue", fg="black", font=("Times New Roman", 12))
registro_button.grid(row=4, column=0, columnspan=2, pady=5)


login.mainloop()    