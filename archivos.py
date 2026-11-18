#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:16/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import pickle
#Funciones
def cargarPersonas():
    """
    Funcionalidad:Cargar la lista de personas desde un archivo binario.
    Entrada:No recibe parámetros.
    Salida:Lista de objetos Persona.
    """
    try:
        archivo=open("personas.pkl", "rb")
        personas=pickle.load(archivo)
        archivo.close()
    except FileNotFoundError:
        personas=[]
    return personas
def guardarPersonas(personas):
    """
    Funcionalidad:Guardar la lista de objetos Persona en un archivo binario.
    Entrada:personas (list), lista de objetos Persona.
    Salida:No retorna valores.
    """
    archivo=open("personas.pkl", "wb")
    pickle.dump(personas,archivo)
    archivo.close()
    
