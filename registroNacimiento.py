#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:25/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import tkinter as tk
from tkinter import ttk,messagebox
import requests
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
    titulo=tk.Label(ventana,text="Datos de la nueva persona",font=("Arial", 16, "bold"))
    titulo.pack(pady=15)
    formulario=tk.Frame(ventana)
    formulario.pack(pady=10)
    #Cita
    tk.Label(formulario, text="Cita:").grid(row=0,column=0)
    cajaCita1=tk.Entry(formulario,width=3)
    cajaCita1.grid(row=0,column=1)
    cajaCita1.config(state="readonly")
    tk.Label(formulario,text="-").grid(row=0,column=2)
    cajaCita2=tk.Entry(formulario,width=6)
    cajaCita2.grid(row=0,column=3)
    tk.Label(formulario,text="-").grid(row=0,column=4)
    cajaCita3=tk.Entry(formulario,width=6)
    cajaCita3.grid(row=0,column=5)
    #Nombre
    tk.Label(formulario,text="Nombre:").grid(row=1,column=0)
    cajaNombre=tk.Entry(formulario,width=30)
    cajaNombre.grid(row=1, column=1,columnspan=5,pady=5)
    #Apellidos
    tk.Label(formulario,text="Apellidos:").grid(row=2,column=0)
    cajaApellidos=tk.Entry(formulario,width=30)
    cajaApellidos.grid(row=2,column=1,columnspan=5,pady=5)
    #Sexo
    ventana.sexo=tk.StringVar(value="")
    tk.Label(formulario, text="Sexo:").grid(row=3,column=0)
    botonMasculino=tk.Radiobutton(formulario,text="Masculino",variable=ventana.sexo,value="M")
    botonMasculino.grid(row=3,column=1, columnspan=2)
    botonFemenino=tk.Radiobutton(formulario,text="Femenino",variable=ventana.sexo,value="F")
    botonFemenino.grid(row=3,column=3,columnspan=3)
    #Distrito
    tk.Label(formulario, text="Distrito:").grid(row=4,column=0)
    cajaDistrito=ttk.Combobox(formulario,width=27,state="disabled")
    cajaDistrito.grid(row=4,column=1,columnspan=5,pady=5)
    #Cantón
    tk.Label(formulario, text="Cantón:").grid(row=5,column=0)
    cajaCanton=ttk.Combobox(formulario,width=27,state="disabled")
    cajaCanton.grid(row=5,column=1,columnspan=5,pady=5)
    #Provincia
    tk.Label(formulario,text="Provincia:").grid(row=6,column=0)
    cajaProvincia=ttk.Combobox(formulario,width=27,state="readonly")
    cajaProvincia.grid(row=6,column=1,columnspan=5,pady=5)
    provincias={}
    def cargarProvincias():
        """
        Funcionalidad:Obtener las provincias desde la API.
        Entrada:No recibe parámetros.
        Salida:No retorna valores.
        """
        try:
            respuesta=requests.get("https://ubicaciones.paginasweb.cr/provincias.json",timeout=10)
            if respuesta.status_code==200:
                provincias.update(respuesta.json())
                cajaProvincia["values"]=list(provincias.values())
            else:
                messagebox.showwarning("Error","No se pudieron cargar las provincias.")
        except (requests.RequestException, ValueError):
            messagebox.showwarning("Error de conexión","No se pudieron cargar las provincias.")
    cargarProvincias()
    cantones={}
    def cargarCantones(event):
        """
        Funcionalidad:Cargar los cantones de la provincia seleccionada.
        Entrada:event,evento de selección.
        Salida:No retorna valores.
        """
        cajaCanton.set("")
        cajaCanton["values"]=[]
        cajaCanton.config(state="disabled")
        cajaDistrito.set("")
        cajaDistrito["values"]=[]
        cajaDistrito.config(state="disabled")
        cantones.clear()
        for codigo,nombre in provincias.items():
            if nombre==cajaProvincia.get():
                cajaCita1.config(state="normal")
                cajaCita1.delete(0,tk.END)
                cajaCita1.insert(0,codigo)
                cajaCita1.config(state="readonly")
                try:
                    respuesta=requests.get(
                        f"https://ubicaciones.paginasweb.cr/provincia/{codigo}/cantones.json",timeout=10)
                    if respuesta.status_code==200:
                        cantones.update(respuesta.json())
                        cajaCanton["values"]=list(cantones.values())
                        cajaCanton.config(state="readonly")
                    else:
                        messagebox.showwarning("Error","No se pudieron cargar los cantones.")
                except (requests.RequestException,ValueError):
                    messagebox.showwarning("Error de conexión","No se pudieron cargar los cantones.")
                break
    cajaProvincia.bind("<<ComboboxSelected>>", cargarCantones)
    distritos={}
    def cargarDistritos(event):
        """
        Funcionalidad:Cargar los distritos del cantón seleccionado.
        Entrada:event,evento de selección.
        Salida:No retorna valores.
        """
        cajaDistrito.set("")
        cajaDistrito["values"]=[]
        cajaDistrito.config(state="disabled")
        distritos.clear()
        codigoProvincia=""
        codigoCanton=""
        for codigo,nombre in provincias.items():
            if nombre==cajaProvincia.get():
                codigoProvincia=codigo
                break
        for codigo,nombre in cantones.items():
            if nombre==cajaCanton.get():
                codigoCanton=codigo
                break
        if codigoProvincia!="" and codigoCanton!="":
            try:
                respuesta=requests.get(
                    f"https://ubicaciones.paginasweb.cr/provincia/{codigoProvincia}/canton/{codigoCanton}/distritos.json",
                    timeout=10)
                if respuesta.status_code==200:
                    distritos.update(respuesta.json())
                    cajaDistrito["values"]=list(distritos.values())
                    cajaDistrito.config(state="readonly")
                else:
                    messagebox.showwarning("Error","No se pudieron cargar los distritos.")
            except (requests.RequestException,ValueError):
                messagebox.showwarning("Error de conexión","No se pudieron cargar los distritos.")
    cajaCanton.bind("<<ComboboxSelected>>", cargarDistritos)
    botonRegresar=tk.Button(ventana,text="Regresar",width=15,command=ventana.destroy)
    botonRegresar.pack(pady=10)
