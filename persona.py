#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:20/11/2026
#Ultima modificacion:122/11/2026
#Version:3.14.7

#Importaciones

#Clase
class Persona:
    """
    Funcionalidad:Representar una persona registrada en el TSE.
    """
    def __init__(self,cedula,nombreCompleto,sexo,ubicacion,fechaNacimiento,padre,nacionalidadPadre,madre,nacionalidadMadre):
        """
        Funcionalidad:Inicializar los datos de una persona.
        Entrada:
        cedula, nombreCompleto, sexo, ubicacion,fechaNacimiento, padre, nacionalidadPadre,madre, nacionalidadMadre (str).
        Salida:No retorna valores.
        """
        self.cedula=cedula
        self.nombreCompleto=nombreCompleto
        self.sexo=sexo
        self.ubicacion=ubicacion
        self.fechaNacimiento=fechaNacimiento
        self.padre=padre
        self.nacionalidadPadre=nacionalidadPadre
        self.madre=madre
        self.nacionalidadMadre=nacionalidadMadre
