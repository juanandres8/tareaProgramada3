#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:20/11/2026
#Ultima modificacion:22/11/2026
#Version:3.14.7

#Importaciones
from archivos import cargarPersonas
#Funciones
personas=cargarPersonas()
print("Total de personas:",len(personas))
for persona in personas:
    print(persona.nombreCompleto)
