import tkinter as tk
from tkinter import messagebox, simpledialog

libros = [
    "El Código da Vinci",
    "El señor de los anillos",
    "El Principito",
    "Don Quijote de la Mancha",
    "El diario de Ana Frank",
    "El Alquimista",
    "Harry Potter – La Colección Completa",
    "Cien años de soledad",
    "El nombre de la rosa",
    "Historia de dos ciudades",
    "Crepúsculo – La saga",
    "Santa Biblia Rvr",
    "El hombre en busca de sentido",
    "La sombra del viento",
    "Piense y Hágase Rico"
]


datos_usuario = {"usuario": None, "contrasena": None}

def iniciar_sesion():
    global ventana_principal
    
    usuario = entrada_usuario.get()
    contrasena = entrada_contrasena.get()
    
    if datos_usuario["usuario"] is None or datos_usuario["contrasena"] is None:
        messagebox.showerror("Error", "Debe registrarse antes de iniciar sesión.")
        return
    
    if usuario == datos_usuario["usuario"] and contrasena == datos_usuario["contrasena"]:
        ventana_login.destroy()
        mostrar_ventana_principal()
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos.")

def registrarse():
    def confirmar_registro():
        global ventana_registro
        
        nuevo_usuario = entrada_nuevo_usuario.get()
        nueva_contrasena = entrada_nueva_contrasena.get()
        
        if nuevo_usuario and nueva_contrasena:
            datos_usuario["usuario"] = nuevo_usuario
            datos_usuario["contrasena"] = nueva_contrasena
            messagebox.showinfo("Registro", "Registro exitoso. Ahora puede iniciar sesión.")
            ventana_registro.destroy()
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese usuario y contraseña.")

    global ventana_registro
    ventana_registro = tk.Toplevel()
    ventana_registro.title("Registrarse")
    ventana_registro.geometry("300x200")
    ventana_registro.configure(bg="black")
    
    etiqueta_nuevo_usuario = tk.Label(ventana_registro, text="Nuevo Usuario", bg="black", fg="white")
    etiqueta_nuevo_usuario.pack()
    
    entrada_nuevo_usuario = tk.Entry(ventana_registro, highlightbackground="green", highlightcolor="green", highlightthickness=2)
    entrada_nuevo_usuario.pack()
    
    etiqueta_nueva_contrasena = tk.Label(ventana_registro, text="Nueva Contraseña", bg="black", fg="white")
    etiqueta_nueva_contrasena.pack()
    
    entrada_nueva_contrasena = tk.Entry(ventana_registro, show="*", highlightbackground="green", highlightcolor="green", highlightthickness=2)
    entrada_nueva_contrasena.pack()
    
    boton_confirmar_registro = tk.Button(ventana_registro, text="Confirmar Registro", command=confirmar_registro, bg="black", fg="white", height=2, width=20)
    boton_confirmar_registro.pack(pady=5)

def mostrar_ventana_principal():
    global ventana_principal
    ventana_principal = tk.Toplevel()
    ventana_principal.title("Biblioteca")
    ventana_principal.geometry("300x300")
    ventana_principal.configure(bg="black")
    
    imagen = tk.PhotoImage(file="logobiblio.jpg").subsample(2)
    label_imagen = tk.Label(ventana_principal, image=imagen, bg="black")
    label_imagen.image = imagen
    label_imagen.pack(pady=20)
    boton_libros_disponibles = tk.Button(ventana_principal, text="Libros Disponibles", command=mostrar_libros, bg="black", fg="white", height=2, width=20)
    boton_libros_disponibles.pack(pady=5)

    boton_rentar_libro = tk.Button(ventana_principal, text="Rentar Libro", command=rentar_libro, bg="black", fg="white", height=2, width=20)
    boton_rentar_libro.pack(pady=5)

def mostrar_libros():
    ventana_libros = tk.Toplevel()
    ventana_libros.title("Libros Disponibles")
    ventana_libros.geometry("400x400")
    ventana_libros.configure(bg="black")

    for libro in libros:
        etiqueta_libro = tk.Label(ventana_libros, text=libro, bg="black", fg="white")
        etiqueta_libro.pack()

def rentar_libro():
    ventana_rentar = tk.Toplevel()
    ventana_rentar.title("Rentar Libro")
    ventana_rentar.geometry("400x400")
    ventana_rentar.configure(bg="black")

    etiqueta_seleccionar = tk.Label(ventana_rentar, text="Seleccione un libro para rentar:", bg="black", fg="white")
    etiqueta_seleccionar.pack(pady=10)

    lista_libros = tk.Listbox(ventana_rentar, selectmode=tk.SINGLE, bg="black", fg="white", highlightbackground="green", highlightcolor="green", highlightthickness=2)
    for libro in libros:
        lista_libros.insert(tk.END, libro)
    lista_libros.pack(pady=10)

    def confirmar_renta():
        seleccion = lista_libros.curselection()
        if seleccion:
            libro_seleccionado = lista_libros.get(seleccion)
            ventana_rentar.destroy()

            dias = simpledialog.askinteger("Rentar Libro", f"¿Por cuántos días desea rentar '{libro_seleccionado}'?", minvalue=1)

            if dias:
                messagebox.showinfo("Rentar Libro", f"Has rentado '{libro_seleccionado}' por {dias} días.")
                libros.remove(libro_seleccionado) 
            else:
                messagebox.showwarning("Advertencia", "Debe ingresar un número válido de días.")

        else:
            messagebox.showwarning("Advertencia", "Seleccione un libro antes de continuar.")

    boton_confirmar_renta = tk.Button(ventana_rentar, text="Confirmar Renta", command=confirmar_renta, bg="black", fg="white", height=2, width=20)
    boton_confirmar_renta.pack(pady=10)

ventana_login = tk.Tk()
ventana_login.title("Biblioteca - Inicio de Sesión")
ventana_login.geometry("300x300")
ventana_login.configure(bg="black")

imagen = tk.PhotoImage(file="logobiblio.jpg").subsample(2)
label_imagen = tk.Label(ventana_login, image=imagen, bg="black")
label_imagen.image = imagen
label_imagen.pack(pady=20)


etiqueta_usuario = tk.Label(ventana_login, text="Usuario", bg="black", fg="white")
etiqueta_usuario.pack()

entrada_usuario = tk.Entry(ventana_login, highlightbackground="green", highlightcolor="green", highlightthickness=2)
entrada_usuario.pack()

etiqueta_contrasena = tk.Label(ventana_login, text="Contraseña", bg="black", fg="white")
etiqueta_contrasena.pack()

entrada_contrasena = tk.Entry(ventana_login, show="*", highlightbackground="green", highlightcolor="green", highlightthickness=2)
entrada_contrasena.pack()


boton_iniciar_sesion = tk.Button(ventana_login, text="Entrar", command=iniciar_sesion, bg="black", fg="white", height=2, width=20)
boton_iniciar_sesion.pack(pady=5)

boton_registrarse = tk.Button(ventana_login, text="Registrarse", command=registrarse, bg="black", fg="white", height=2, width=20)
boton_registrarse.pack(pady=5)


ventana_login.mainloop()
