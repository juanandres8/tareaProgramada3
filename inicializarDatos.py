#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:22/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
from archivos import cargarPersonas, guardarPersonas
from datosIniciales import crearDatosIniciales
#Funciones
personas=cargarPersonas()
datosIniciales=crearDatosIniciales()
for nuevaPersona in datosIniciales:
    existe=False
    for persona in personas:
        if persona.cedula==nuevaPersona.cedula:
            existe = True
            break
    if existe==False:
        personas.append(nuevaPersona)
guardarPersonas(personas)
print("Total de personas guardadas:", len(personas))
for persona in personas:
    print(persona.cedula, persona.nombreCompleto)

