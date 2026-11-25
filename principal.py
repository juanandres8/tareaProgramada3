#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:20/11/2026
#Ultima modificacion:22/11/2026
#Version:3.14.7

#Importaciones
from archivos import cargarPersonas
from ventanaPrincipal import mostrarVentanaPrincipal
import registro
#Funciones
if registro.accesoAutorizado:
    personas=cargarPersonas()
    mostrarVentanaPrincipal(personas)
