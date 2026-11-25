# Elaborado por: Fabiana Quesada y Juan Arias
# Fecha de creación: 24/11/2026
# Versión: 3.14.7

# Importaciones
from tkinter import *
from tkinter import messagebox
import re
import os

accesoAutorizado=False
# Funciones
def limpiar():
    """
    Funcionalidad: Limpiar las cajas de texto.
    Entrada: No recibe parámetros.
    Salida: No retorna valores.
    """
    cajaUsuario.delete(0, END)
    cajaContrasena.delete(0, END)

def validarUsuario(usuario):
    """
    Funcionalidad: Validar el formato del correo electrónico.
    Entrada: usuario (str).
    Salida: Boolean.
    """
    patron = r"^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$"
    return re.match(patron, usuario) is not None

def validarContrasena(contrasena):
    """
    Funcionalidad: Validar los requisitos de la contraseña.
    Entrada: contrasena (str).
    Salida: Boolean.
    """
    if len(contrasena) < 5 or len(contrasena) > 15:
        return False
    tieneNumero = False
    tieneLetra = False
    for caracter in contrasena:
        if caracter.isdigit():
            tieneNumero = True
        if caracter.isalpha():
            tieneLetra = True
    return tieneNumero and tieneLetra

def leerArchivo(usuario, contrasena):
    """
    Funcionalidad: Leer el archivo de texto y verificar
    si el usuario está autorizado.
    Si no existe, lo crea.
    """
    ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)),"usuarios.txt")
    try:
        archivo = open(ruta, "r")
    except FileNotFoundError:
        archivo = open(ruta, "w")
        archivo.close()
        return False
    autorizado = False
    for linea in archivo:
        datos = linea.strip().split(",")
        if len(datos) == 2:
            usuarioArchivo = datos[0].strip().lower()
            contrasenaArchivo = datos[1].strip()
            usuarioIngresado = usuario.strip().lower()
            if (usuarioIngresado == usuarioArchivo and
                contrasena == contrasenaArchivo):
                autorizado = True
    archivo.close()
    return autorizado

def ingresar():
    """
    Funcionalidad: Validar los datos e ingresar al sistema.
    Entrada: No recibe parámetros.
    Salida: No retorna valores.
    """
    global accesoAutorizado
    usuario = cajaUsuario.get().strip()
    contrasena = cajaContrasena.get()
    if usuario == "" or contrasena == "":
        messagebox.showwarning("Advertencia","Debe completar todos los campos.")
    elif not validarUsuario(usuario):
        messagebox.showerror("Error","El usuario debe tener formato de correo electrónico.")
    elif not validarContrasena(contrasena):
        messagebox.showerror( "Error","La contraseña debe tener entre 5 y 15 caracteres,\n""al menos una letra y un número.")
    elif leerArchivo(usuario, contrasena):
        accesoAutorizado=True
        messagebox.showinfo("Acceso autorizado","Bienvenido al sistema del Tribunal Supremo de Elecciones." )
        ventana.destroy()
    else:
        messagebox.showerror( "Acceso denegado", "El usuario o la contraseña son incorrectos.")

# Ventana de registro
ventana = Tk()
ventana.title("Registro de usuario")
ventana.geometry("400x250")
ventana.resizable(False, False)

# Título
titulo = Label(ventana,
    text="Tribunal Supremo de Elecciones",
    font=("Arial", 14, "bold"))
titulo.pack(pady=15)
# Usuario
etiquetaUsuario = Label( ventana,text="Usuario:")
etiquetaUsuario.pack()
cajaUsuario = Entry(ventana,width=30)
cajaUsuario.pack(pady=5)
# Contraseña
etiquetaContrasena = Label(ventana,text="Contraseña:")
etiquetaContrasena.pack()
cajaContrasena = Entry( ventana,width=30,show="*")
cajaContrasena.pack(pady=5)
# Botones
botones = Frame(ventana)
botones.pack(pady=20)
botonIngresar = Button(botones,text="Ingresar",width=12,command=ingresar)
botonIngresar.grid(row=0, column=0, padx=10)
botonLimpiar = Button(botones,text="Limpiar",width=12,command=limpiar)
botonLimpiar.grid(row=0, column=1, padx=10)

ventana.mainloop()
