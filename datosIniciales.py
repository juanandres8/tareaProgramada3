#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:16/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
from persona import Persona
#Funciones
def crearDatosIniciales():
    """
    Funcionalidad:Crear los objetos iniciales de personas para el sistema del TSE.
    Entrada:No recibe parámetros.
    Salida:Lista de objetos Persona.
    """
    personas=[]
    persona1=Persona(
        "3-0100-0001",
        "Carlos Rodríguez Mora",
        "M","Oriental Central Cartago","15/03/1965","","","","")
    persona2=Persona(
        "3-0100-0002",
        "María Fernández López",
        "F","Oriental Central Cartago","20/07/1968","","","","")
    persona3=Persona(
        "1-0100-0003",
        "José Vargas Ruiz",
        "M","Carmen Central San José","12/04/1962","","","","")
    persona4=Persona(
        "2-0100-0004",
        "Laura Salazar Rojas",
        "F","Alajuela Alajuela Alajuela","08/09/1967","","","","")
    persona5=Persona(
        "3-0100-0005",
        "Luis Jiménez Soto",
        "M","Oriental Central Cartago","21/06/1964","","","","")
    persona6=Persona(
        "4-0100-0006",
        "Patricia Campos Solís",
        "F","Mercedes Heredia Heredia","14/11/1970","","","","")
    persona7=Persona(
        "5-0100-0007",
        "Ricardo Méndez León",
        "M","Liberia Liberia Guanacaste","03/02/1963","","","","")
    persona8=Persona(
        "6-0100-0008",
        "Sofía Núñez Castro",
        "F","Puntarenas Puntarenas Puntarenas","18/08/1970","","","","")
    persona9=Persona(
        "7-0100-0009",
        "Miguel Chaves Arias",
        "M","Limón Limón Limón","25/01/1961","","","","")
    persona10=Persona(
        "1-0100-0010",
        "Daniela Herrera Monge",
        "F","Carmen Central San José","30/05/1971","","","","")
    personas.append(persona1)
    personas.append(persona2)
    personas.append(persona3)
    personas.append(persona4)
    personas.append(persona5)
    personas.append(persona6)
    personas.append(persona7)
    personas.append(persona8)
    personas.append(persona9)
    personas.append(persona10)
    return personas
