#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:24/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import tkinter as tk
from registroNacimiento import *
#Funciones
def mostrarVentanaPrincipal(personas):
    """
    Funcionalidad: Mostrar la ventana principal del sistema TSE.
    Entrada: Lista de objetos Persona.
    Salida: No retorna valores.
    """
    ventana=tk.Tk()
    ventana.title("Tribunal Supremo de Elecciones")
    ventana.geometry("450x400")
    titulo=tk.Label(
        ventana,text="Tribunal Supremo de Elecciones",font=("Arial", 16, "bold"))
    titulo.pack(pady=20)
    total=tk.Label(ventana,text="Total de personas: "+str(len(personas)))
    total.pack(pady=5)
    def actualizarTotal():
        """
        Funcionalidad:Actualizar la cantidad de personas registradas en la ventana principal.
        Entrada:No recibe parámetros.
        Salida:No retorna valores.
        """
        total.config(text="Total de personas: "+str(len(personas)))
    #botonRegistrar
    botonRegistrar = tk.Button(
        ventana,text="Registrar Nacimiento",width=25,command=lambda: mostrarRegistroNacimiento(ventana, personas,actualizarTotal))
    botonRegistrar.pack(pady=5)
    #botonArbol
    botonArbol=tk.Button(
        ventana,text="Mostrar árbol genealógico",width=25,state="disabled")
    botonArbol.pack(pady=5)
    botonCertificado=tk.Button(
        ventana,text="Certificado de Nacimiento",width=25,state="disabled")
    botonCertificado.pack(pady=5)
   #BotonRegistro
    botonReportes=tk.Button(ventana,text="Reportes",width=25,command=lambda: mostrarReportes(ventana, personas))
    botonReportes.pack(pady=5)
    
    botonSalir=tk.Button(
        ventana,text="Salir",width=25,command=ventana.destroy)
    botonSalir.pack(pady=5)
    ventana.mainloop()
