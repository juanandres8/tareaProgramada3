#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:25/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import tkinter as tk
from tkinter import ttk,messagebox
import requests
import json
import re
from datetime import date
from persona import Persona
from archivos import *
#Funciones
def mostrarRegistroNacimiento(ventanaPrincipal, personas, actualizarTotal):
    """
    Funcionalidad:Mostrar la ventana para registrar un nuevo nacimiento y actualiza la cantidad de personas registradas.
    Entrada:ventanaPrincipal, lista de objetos Persona y actualizar el total de personas.
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
    #Día
    tk.Label(formulario,text="Día:").grid(row=7,column=0)
    cajaDia=ttk.Combobox(
        formulario,values=list(range(1, 32)),width=12,state="readonly")
    cajaDia.grid(row=7,column=1,columnspan=5,pady=5)
    #Mes
    tk.Label(formulario,text="Mes:").grid(row=8,column=0)
    cajaMes=ttk.Combobox(
        formulario,values=list(range(1, 13)),width=12,state="readonly")
    cajaMes.grid(row=8,column=1,columnspan=5,pady=5)
    #Año
    tk.Label(formulario,text="Año:").grid(row=9,column=0)
    cajaAnio=ttk.Combobox(formulario,values=list(range(1900, 2027)),width=12,state="readonly")
    cajaAnio.grid(row=9,column=1, columnspan=5,pady=5)
    #Obtener los padres y madres disponibles
    padres=[]
    madres=[]
    for persona in personas:
        opcion=persona.cedula+" "+persona.nombreCompleto
        if persona.sexo=="M":
            padres.append(opcion)
        elif persona.sexo=="F":
            madres.append(opcion)
    #Padre
    tk.Label(formulario,text="Padre:").grid(row=10, column=0)
    cajaPadre=ttk.Combobox(formulario,values=padres,width=27,state="readonly")
    cajaPadre.grid(row=10,column=1,columnspan=5,pady=5)
    # Madre
    tk.Label(formulario,text="Madre:").grid(row=12,column=0)
    cajaMadre=ttk.Combobox(formulario,values=madres,width=27,state="readonly")
    cajaMadre.grid(row=12,column=1,columnspan=5,pady=5)
    #Nacionalidades disponibles
    nacionalidades=["Costarricense","Nicaragüense","Estadounidense","Canadiense","Español"]
    #Nacionalidad del padre
    tk.Label(formulario,text="Nacionalidad:").grid(row=11,column=0)
    cajaNacionalidadPadre=ttk.Combobox(formulario,values=nacionalidades,width=27,state="readonly")
    cajaNacionalidadPadre.grid(row=11,column=1,columnspan=5,pady=5)
    cajaNacionalidadPadre.set("Costarricense")
    #Nacionalidad de la madre
    tk.Label(formulario,text="Nacionalidad:").grid(row=13,column=0)
    cajaNacionalidadMadre=ttk.Combobox(formulario,values=nacionalidades,width=27,state="readonly")
    cajaNacionalidadMadre.grid(row=13,column=1,columnspan=5,pady=5)
    cajaNacionalidadMadre.set("Costarricense")
    provincias={}
    def cargarProvincias():
        """
        Funcionalidad:Cargar las provincias desde la API o desde el archivo de respaldo.
        Entrada:No recibe parámetros.
        Salida:No retorna valores.
        """
        cargado=False
        try:
            respuesta=requests.get("https://ubicaciones.paginasweb.cr/provincias.json",timeout=10)
            if respuesta.status_code==200:
                datos=respuesta.json()
                if isinstance(datos, dict) and len(datos)>0:
                    provincias.update(datos)
                    cargado=True
        except (requests.RequestException,ValueError):
            cargado=False
        if cargado==False:
            messagebox.showwarning("Error de conexión","No se pudo consultar la API. Se utilizará el respaldo local.",parent=ventana) 
            try:
                with open("ubicaciones.json", "r", encoding="utf-8") as archivo:
                    respaldo=json.load(archivo)
                for codigo,datos in respaldo.items():
                    provincias[codigo]=datos["nombre"]
            except (OSError,ValueError,KeyError,TypeError):
                messagebox.showerror("Error","No se pudo cargar el archivo de respaldo.")
        cajaProvincia["values"]=list(provincias.values())
    cargarProvincias()
    ventana.lift()
    cantones={}
    def cargarCantones(event):
        """
        Funcionalidad:Cargar los cantones de la provincia seleccionada desde la API o el respaldo.
        Entrada:event, evento de selección.
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
                cajaCita1.delete(0, tk.END)
                cajaCita1.insert(0, codigo)
                cajaCita1.config(state="readonly")
                cargado=False
                try:
                    respuesta=requests.get(
                        f"https://ubicaciones.paginasweb.cr/provincia/{codigo}/cantones.json",timeout=10)
                    if respuesta.status_code==200:
                        datos=respuesta.json()
                        if isinstance(datos, dict) and len(datos)>0:
                            cantones.update(datos)
                            cargado=True
                except (requests.RequestException,ValueError):
                    cargado=False
                if cargado==False:
                    messagebox.showwarning(
                        "Error de conexión","Se utilizarán los cantones del respaldo local.",parent=ventana)
                    try:
                        with open("ubicaciones.json", "r", encoding="utf-8") as archivo:
                            respaldo=json.load(archivo)
                        datosCantones=respaldo[codigo]["cantones"]
                        for codigoCanton, datos in datosCantones.items():
                            cantones[codigoCanton]=datos["nombre"]
                    except (OSError, ValueError, KeyError, TypeError):
                        messagebox.showerror(
                            "Error","No se pudieron cargar los cantones del respaldo.",parent=ventana)
                if len(cantones)>0:
                    cajaCanton["values"]=list(cantones.values())
                    cajaCanton.config(state="readonly")
                break
    cajaProvincia.bind("<<ComboboxSelected>>", cargarCantones)
    distritos={}
    def cargarDistritos(event):
        """
        Funcionalidad:Cargar los distritos del cantón seleccionado desde la API o el respaldo.
        Entrada:event, evento de selección.
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
            cargado=False
            try:
                respuesta=requests.get(
                    f"https://ubicaciones.paginasweb.cr/provincia/{codigoProvincia}/canton/{codigoCanton}/distritos.json",
                    timeout=10)
                if respuesta.status_code==200:
                    datos=respuesta.json()
                    if isinstance(datos, dict) and len(datos)>0:
                        distritos.update(datos)
                        cargado=True
            except (requests.RequestException, ValueError):
                cargado=False
            if cargado==False:
                messagebox.showwarning(
                    "Error de conexión",
                    "Se utilizarán los distritos del respaldo local.",parent=ventana)
                try:
                    with open("ubicaciones.json", "r",encoding="utf-8") as archivo:
                        respaldo=json.load(archivo)
                    datosDistritos=respaldo[codigoProvincia]["cantones"][codigoCanton]["distritos"]
                    distritos.update(datosDistritos)
                except (OSError, ValueError, KeyError, TypeError):
                    messagebox.showerror(
                        "Error",
                        "No se pudieron cargar los distritos del respaldo.",
                        parent=ventana)
            if len(distritos)>0:
                cajaDistrito["values"]=list(distritos.values())
                cajaDistrito.config(state="readonly")
    cajaCanton.bind("<<ComboboxSelected>>", cargarDistritos)
    def limpiarCampos():
        """
        Funcionalidad:Limpiar los campos del formulario de registro de nacimiento.
        Entrada:No recibe parámetros.
        Salida:No retorna valores.
        """
        cajaCita1.config(state="normal")
        cajaCita1.delete(0,tk.END)
        cajaCita1.config(state="readonly")
        cajaCita2.delete(0,tk.END)
        cajaCita3.delete(0,tk.END)
        cajaNombre.delete(0,tk.END)
        cajaApellidos.delete(0,tk.END)
        ventana.sexo.set("")
        cajaProvincia.set("")
        cajaCanton.set("")
        cajaCanton["values"]=[]
        cajaCanton.config(state="disabled")
        cajaDistrito.set("")
        cajaDistrito["values"]=[]
        cajaDistrito.config(state="disabled")
        cantones.clear()
        distritos.clear()
        cajaDia.set("")
        cajaMes.set("")
        cajaAnio.set("")
        cajaPadre.set("")
        cajaMadre.set("")
        cajaNacionalidadPadre.set("Costarricense")
        cajaNacionalidadMadre.set("Costarricense")
    def validarCampos():
        """
        Funcionalidad:Verificar que los campos del registro estén completos.
        Entrada:No recibe parámetros.
        Salida:True si están completos,False si falta alguno.
        """
        if cajaCita1.get()=="" or cajaCita2.get()=="" or cajaCita3.get()=="":
            messagebox.showwarning("Advertencia","Debe completar la cita.",parent=ventana)
            return False
        if cajaNombre.get().strip()=="" or cajaApellidos.get().strip()=="":
            messagebox.showwarning("Advertencia","Debe completar el nombre y los apellidos.",parent=ventana)
            return False
        if ventana.sexo.get()=="":
            messagebox.showwarning("Advertencia","Debe seleccionar el sexo.",parent=ventana)
            return False
        if cajaProvincia.get()=="" or cajaCanton.get()=="" or cajaDistrito.get()=="":
            messagebox.showwarning("Advertencia","Debe seleccionar la ubicación completa.",parent=ventana)
            return False
        cita=cajaCita1.get()+"-"+cajaCita2.get()+"-"+cajaCita3.get()
        if re.match(r"^[1-7]-[0-9]{4}-[0-9]{4}$",cita)==None:
            messagebox.showwarning("Advertencia","La cita debe tener el formato 3-0234-0987.",parent=ventana)
            return False
        codigoProvincia=""
        for codigo, nombre in provincias.items():
            if nombre==cajaProvincia.get():
                codigoProvincia=codigo
                break
        if cajaCita1.get()!=codigoProvincia:
            messagebox.showwarning("Advertencia","El primer número de la cita no corresponde a la provincia.",parent=ventana)
            return False
        if cajaDia.get()=="" or cajaMes.get()=="" or cajaAnio.get()=="":
            messagebox.showwarning("Advertencia","Debe seleccionar la fecha de nacimiento.",parent=ventana)
            return False
        try:
            fechaNacimiento=date(int(cajaAnio.get()),int(cajaMes.get()),int(cajaDia.get()))
        except ValueError:
            messagebox.showwarning("Advertencia","La fecha de nacimiento no es válida.",parent=ventana)
            return False
        if fechaNacimiento>date.today():
            messagebox.showwarning("Advertencia","La fecha de nacimiento no puede ser futura.",parent=ventana)
            return False
        if cajaPadre.get()=="" or cajaMadre.get()=="":
            messagebox.showwarning("Advertencia","Debe seleccionar el padre y la madre.",parent=ventana)
            return False
        cita=cajaCita1.get()+"-"+cajaCita2.get()+"-"+cajaCita3.get()
        for persona in personas:
            if persona.cedula==cita:
                messagebox.showwarning("Advertencia","La persona ya se encuentra registrada.",parent=ventana)
                return False
        return True
    def registrarNacimiento():
        """
        Funcionalidad:Registrar una nueva persona y guardar sus datos en el archivo binario.
        Entrada:No recibe parámetros.
        Salida:No retorna valores.
        """
        if validarCampos()==False:
            return
        cedula=cajaCita1.get()+"-"+cajaCita2.get()+"-"+cajaCita3.get()
        nombreCompleto=cajaNombre.get().strip()+" "+cajaApellidos.get().strip()
        sexo=ventana.sexo.get()
        ubicacion=cajaDistrito.get()+" "+cajaCanton.get()+" "+cajaProvincia.get()
        fechaNacimiento=cajaDia.get().zfill(2)+"/"+cajaMes.get().zfill(2)+"/"+cajaAnio.get()
        padre=""
        madre=""
        for persona in personas:
            if cajaPadre.get()==persona.cedula+" "+persona.nombreCompleto:
                padre=persona.nombreCompleto
            if cajaMadre.get()==persona.cedula+" "+persona.nombreCompleto:
                madre=persona.nombreCompleto
        nuevaPersona=Persona(cedula,nombreCompleto,sexo,ubicacion,fechaNacimiento,padre,cajaNacionalidadPadre.get(),madre,cajaNacionalidadMadre.get())
        personas.append(nuevaPersona)
        try:
            guardarPersonas(personas)
        except OSError:
            personas.remove(nuevaPersona)
            messagebox.showerror("Error","No se pudo guardar el registro.",parent=ventana)
            return
        actualizarTotal()
        messagebox.showinfo("Registro exitoso","La persona fue registrada correctamente.",parent=ventana)
        limpiarCampos()
    #Botones
    botones=tk.Frame(ventana)
    botones.pack(pady=10)
    botonRegistrar=tk.Button(botones, text="Registrar", width=15,command=registrarNacimiento)
    botonRegistrar.grid(row=0,column=0,padx=5)
    botonLimpiar=tk.Button(botones, text="Limpiar", width=15,command=limpiarCampos)
    botonLimpiar.grid(row=0,column=1, padx=5)
    botonRegresar=tk.Button(botones, text="Regresar", width=15,command=ventana.destroy)
    botonRegresar.grid(row=0,column=2,padx=5)
