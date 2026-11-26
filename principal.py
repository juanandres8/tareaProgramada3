#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:20/11/2026
#Ultima modificacion:22/11/2026
#Version:3.14.7

#Importaciones
from archivos import *
from datosIniciales import crearDatosIniciales
from ventanaPrincipal import mostrarVentanaPrincipal
import registro
#Funciones
if registro.accesoAutorizado:
    personas=cargarPersonas()
    if len(personas)==0:
        personas=crearDatosIniciales()
        guardarPersonas(personas)
    mostrarVentanaPrincipal(personas)
