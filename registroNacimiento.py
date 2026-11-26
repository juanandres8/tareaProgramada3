#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:24/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import tkinter as tk
#Funciones
def mostrarRegistroNacimiento(ventanaPrincipal, personas):
    """
    Funcionalidad:Mostrar la ventana para registrar un nuevo nacimiento.
    Entrada:ventanaPrincipal y lista de objetos Persona.
    Salida:No retorna valores.
    """
    ventana=tk.Toplevel(ventanaPrincipal)
    ventana.title("Registro de Nacimiento")
    ventana.geometry("550x600")
    titulo=tk.Label(
        ventana,text="Datos de la nueva persona",font=("Arial", 16, "bold"))
    titulo.pack(pady=15)
    formulario=tk.Frame(ventana)
    formulario.pack(pady=10)
    botonRegresar=tk.Button(
        ventana,text="Regresar",width=15,command=ventana.destroy)
    botonRegresar.pack(pady=10)
