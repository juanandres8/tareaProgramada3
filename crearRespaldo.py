#Elaborado por: Fabiana Quesada y Juan Arias
#Fecha de creación:25/11/2026
#Ultima modificacion:16/11/2026
#Version:3.14.7

#Importaciones
import requests
import json
#Funciones
def consultarDatos(url):
    """
    Funcionalidad:Consultar datos desde la API.
    Entrada:URL del servicio.
    Salida:Datos obtenidos o None si falla.
    """
    respuesta=requests.get(url,timeout=10)
    if respuesta.status_code==200:
        return respuesta.json()
    return None
def crearRespaldo():
    """
    Funcionalidad:Crear un archivo JSON con las provincias,cantones y distritos de Costa Rica.
    Entrada: No recibe parámetros.
    Salida: No retorna valores.
    """
    respaldo={}
    try:
        provincias=consultarDatos("https://ubicaciones.paginasweb.cr/provincias.json")
        if provincias is None:
            print("No se pudieron obtener las provincias.")
            return
        for codigoProvincia, nombreProvincia in provincias.items():
            url=f"https://ubicaciones.paginasweb.cr/provincia/{codigoProvincia}/cantones.json"
            cantones=consultarDatos(url)
            if cantones is None:
                print("Error al obtener cantones.")
                return
            respaldo[codigoProvincia]={"nombre": nombreProvincia,"cantones": {}}
            for codigoCanton,nombreCanton in cantones.items():
                url=f"https://ubicaciones.paginasweb.cr/provincia/{codigoProvincia}/canton/{codigoCanton}/distritos.json"
                distritos=consultarDatos(url)
                if distritos is None:
                    print("Error al obtener distritos.")
                    return
                respaldo[codigoProvincia]["cantones"][codigoCanton]={"nombre":nombreCanton,"distritos": distritos}
            print("Provincia procesada:", nombreProvincia)
        archivo=open("ubicaciones.json", "w", encoding="utf-8")
        json.dump(respaldo, archivo, ensure_ascii=False, indent=4)
        archivo.close()
        print("Archivo de respaldo creado correctamente.")

    except (requests.RequestException, ValueError):
        print("Error de conexión. No se pudo crear el respaldo.")


crearRespaldo()
