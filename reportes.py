# Elaborado por: Fabiana Quesada y Juan Arias
# Fecha de creación: 26/11/2026
# Versión: 3.14.7

# Importaciones
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re
import html

# Funciones
def generarHTML(titulo, contenido, nombreArchivo):
    """
    Funcionalidad: Crear un archivo HTML con la información del reporte.
    Entrada: titulo, contenido y nombreArchivo (str).
    Salida: No retorna valores.
    """
    archivo = open(nombreArchivo, "w", encoding="utf-8")
    archivo.write("""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>""" + html.escape(titulo) + """</title>
        <style>
            body {font-family: Arial;margin: 30px;}
            h1 {text-align: center;}
            table {width: 100%;border-collapse: collapse;}
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: left;}
            th {background-color: #dddddd;}
        </style>
    </head>
    <body>
        <h1>""" + html.escape(titulo) + """</h1>
        """ + contenido + """
    </body>
    </html>
    """)
    archivo.close()

def crearTabla(personas, incluirPadres=False):
    """
    Funcionalidad: Crear una tabla HTML con los datos de las personas.
    Entrada: personas (list), incluirPadres (bool).
    Salida: Tabla HTML (str).
    """
    tabla = """
    <table>
        <tr>
            <th>Cédula</th>
            <th>Nombre completo</th>
            <th>Fecha de nacimiento</th>
            <th>Sexo</th>
    """
    if incluirPadres:
        tabla += """
            <th>Madre</th>
            <th>Padre</th>
        """
    tabla += "</tr>"
    for persona in personas:
        tabla += "<tr>"
        tabla += "<td>" + html.escape(persona.cedula) + "</td>"
        tabla += "<td>" + html.escape(persona.nombreCompleto) + "</td>"
        tabla += "<td>" + html.escape(persona.fechaNacimiento) + "</td>"
        if persona.sexo == "F":
            sexo = "Femenino"
        else:
            sexo = "Masculino"
        tabla += "<td>" + sexo + "</td>"
        if incluirPadres:
            tabla += "<td>" + html.escape(persona.madre) + "</td>"
            tabla += "<td>" + html.escape(persona.padre) + "</td>"
        tabla += "</tr>"
    tabla += "</table>"
    return tabla

def obtenerProvincia(persona):
    """
    Funcionalidad: Obtener la provincia desde la ubicación.
    Entrada: persona (Persona).
    Salida: Nombre de la provincia (str).
    """
    partes = persona.ubicacion.strip().split()
    if len(partes) >= 3:
        return partes[-1].lower()
    return ""

def obtenerTomo(persona):
    """
    Funcionalidad: Obtener el tomo desde la cédula.
    Entrada: persona (Persona).
    Salida: Tomo (str).
    """
    partes = persona.cedula.split("-")
    if len(partes) == 3:
        return partes[1]
    return ""

def obtenerAnio(persona):
    """
    Funcionalidad: Obtener el año de nacimiento.
    Entrada: persona (Persona).
    Salida: Año (int) o None.
    """
    partes = persona.fechaNacimiento.split("/")
    if len(partes) == 3:
        try:
            return int(partes[2])
        except ValueError:
            return None
    return None

def crearReporteProvincia(personas, provincia):
    """
    Funcionalidad: Generar el reporte de personas por provincia.
    Entrada: personas (list), provincia (str).
    Salida: No retorna valores.
    """
    lista = []
    for persona in personas:
        if obtenerProvincia(persona) == provincia.lower():
            lista.append(persona)
    mujeres = []
    hombres = []
    for persona in lista:
        if persona.sexo == "F":
            mujeres.append(persona)
        else:
            hombres.append(persona)
    listaOrdenada = mujeres + hombres
    if len(listaOrdenada) == 0:
        messagebox.showwarning(
            "Sin resultados",
            "No hay personas registradas en esa provincia.")
        return
    contenido = crearTabla(listaOrdenada)
    generarHTML("Personas registradas en " + provincia,contenido,"reporte_provincia.html")
    messagebox.showinfo("Reporte creado","Se creó el archivo reporte_provincia.html correctamente." )

def crearReporteAnio(personas, anio):
    """
    Funcionalidad: Generar un reporte de personas nacidas
    a partir del año indicado, agrupadas por año.
    Entrada: personas (list), anio (int).
    Salida: No retorna valores.
    """
    grupos = {}
    for persona in personas:
        anioNacimiento = obtenerAnio(persona)
        if anioNacimiento is not None and anioNacimiento >= anio:
            if anioNacimiento not in grupos:
                grupos[anioNacimiento] = []
            grupos[anioNacimiento].append(persona)
    if len(grupos) == 0:
        messagebox.showwarning("Sin resultados","No hay personas nacidas a partir de ese año.")
        return
    contenido = ""
    for anioNacimiento in sorted(grupos):
        contenido += "<h2>Año: " + str(anioNacimiento) + "</h2>"
        contenido += crearTabla(grupos[anioNacimiento], True)
    generarHTML("Personas nacidas a partir de " + str(anio),contenido, "reporte_anios.html")
    messagebox.showinfo( "Reporte creado","Se creó el archivo reporte_anios.html correctamente.")

def crearReporteHospital(personas, tomo):
    """
    Funcionalidad: Generar un reporte de personas del mismo hospital.
    Entrada: personas (list), tomo (str).
    Salida: No retorna valores.
    """
    lista = []
    for persona in personas:
        if obtenerTomo(persona) == tomo:
            lista.append(persona)
    hombres = []
    mujeres = []
    for persona in lista:
        if persona.sexo == "M":
            hombres.append(persona)
        else:
            mujeres.append(persona)
    listaOrdenada = hombres + mujeres
    if len(listaOrdenada) == 0:
        messagebox.showwarning("Sin resultados","No hay personas registradas en ese hospital." )
        return
    contenido = crearTabla(listaOrdenada, True)
    generarHTML("Personas registradas en el hospital - Tomo " + tomo,
        contenido,"reporte_hospital.html")
    messagebox.showinfo("Reporte creado","Se creó el archivo reporte_hospital.html correctamente.")

def mostrarReportes(ventanaPrincipal, personas):
    """
    Funcionalidad: Mostrar la ventana de reportes.
    Entrada: ventanaPrincipal y lista de personas.
    Salida: No retorna valores.
    """
    ventana = tk.Toplevel(ventanaPrincipal)
    ventana.title("Reportes")
    ventana.geometry("500x450")
    ventana.resizable(False, False)
    titulo = tk.Label(ventana,text="Reportes del TSE",font=("Arial", 16, "bold"))
    titulo.pack(pady=15)
    # Reporte por provincia
    marcoProvincia = tk.LabelFrame(ventana,text="Personas por provincia",
        padx=15,
        pady=10)
    marcoProvincia.pack(fill="x", padx=20, pady=8)
    provincias = [
        "San José",
        "Alajuela",
        "Cartago",
        "Heredia",
        "Guanacaste",
        "Puntarenas",
        "Limón"]
    seleccionProvincia = tk.StringVar()
    cajaProvincia = ttk.Combobox(
        marcoProvincia,
        textvariable=seleccionProvincia,
        values=provincias,
        state="readonly",
        width=25)
    cajaProvincia.pack(pady=5)
    botonProvincia = tk.Button(
        marcoProvincia,
        text="Crear",
        state="disabled",
        command=lambda: crearReporteProvincia(
            personas,
            seleccionProvincia.get()))
    botonProvincia.pack(pady=5)
    def validarProvincia(event=None):
        if seleccionProvincia.get() != "":
            botonProvincia.config(state="normal")
        else:
            botonProvincia.config(state="disabled")
    cajaProvincia.bind("<<ComboboxSelected>>", validarProvincia)
    # Reporte por año
    marcoAnio = tk.LabelFrame(ventana,text="Personas nacidas a partir de...",
        padx=15,
        pady=10)
    marcoAnio.pack(fill="x", padx=20, pady=8)
    entradaAnio = tk.Entry(
        marcoAnio,
        width=20)
    entradaAnio.pack(pady=5)
    botonAnio = tk.Button( marcoAnio,text="Crear",state="disabled",
        command=lambda: crearReporteAnio(personas,int(entradaAnio.get())))
    botonAnio.pack(pady=5)
    def validarAnio(event=None):
        anio = entradaAnio.get()
        if re.fullmatch(r"\d{4}", anio):
            botonAnio.config(state="normal")
        else:
            botonAnio.config(state="disabled")
    entradaAnio.bind("<KeyRelease>", validarAnio)
    # Reporte por hospital
    marcoHospital = tk.LabelFrame(ventana,text="Personas del mismo hospital",
        padx=15,pady=10)
    marcoHospital.pack(fill="x", padx=20, pady=8)
    tomos = []
    for persona in personas:
        tomo = obtenerTomo(persona)
        if tomo != "" and tomo not in tomos:
            tomos.append(tomo)
    tomos.sort()
    seleccionTomo = tk.StringVar()
    cajaHospital = ttk.Combobox(marcoHospital,textvariable=seleccionTomo,
        values=tomos,state="readonly",width=25)
    cajaHospital.pack(pady=5)
    botonHospital = tk.Button(marcoHospital,text="Crear", state="disabled",
        command=lambda: crearReporteHospital(personas,seleccionTomo.get()))
    botonHospital.pack(pady=5)
    def validarHospital(event=None):
        if seleccionTomo.get() != "":
            botonHospital.config(state="normal")
        else:
            botonHospital.config(state="disabled")
    cajaHospital.bind("<<ComboboxSelected>>", validarHospital)
    # Botón regresar
    botonRegresar = tk.Button( ventana, text="Regresar", width=15, command=ventana.destroy )
    botonRegresar.pack(pady=12)
