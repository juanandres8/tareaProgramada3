#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:24/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import tkinter as tk
#Funciones
def mostrarVentanaPrincipal(personas):
    """
    Funcionalidad: Mostrar la ventana principal del sistema TSE.
    Entrada: Lista de objetos Persona.
    Salida: No retorna valores.
    """
    ventana=tk.Tk()
    ventana.title("Tribunal Supremo de Elecciones")
    ventana.geometry("450x350")
    titulo=tk.Label(
        ventana,text="Tribunal Supremo de Elecciones",font=("Arial", 16, "bold"))
    titulo.pack(pady=20)
    total=tk.Label(
        ventana,text="Total de personas: "+str(len(personas)))
    total.pack(pady=5)
    ventana.mainloop()
