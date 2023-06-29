from modules.file_operations import Archivo
from modules.directory_operations import Directorio
from chats.chart_generation import generar_grafica

def procesar_comando(comando, directorio_actual):
    partes = comando.split(" ")
    accion = partes[0]

    if accion == "crear_archivo":
        nombre_archivo = partes[1]
        directorio_actual.crear_archivo(nombre_archivo)
    elif accion == "renombrar_archivo":
        viejo_nombre = partes[1]
        nuevo_nombre = partes[2]
        archivos = directorio_actual.listar_archivos()
        archivo_encontrado = None
        for archivo in archivos:
            if archivo.nombre == viejo_nombre:
                archivo_encontrado = archivo
                break
        if archivo_encontrado:
            archivo_encontrado.renombrar(nuevo_nombre)
        else:
            print(f"No se encontró el archivo {viejo_nombre}")
    elif accion == "eliminar_archivo":
        nombre_archivo = partes[1]
        # Lógica para encontrar y eliminar el archivo
        archivos = directorio_actual.listar_archivos()
        archivo_encontrado = None
        for archivo in archivos:
            if archivo.nombre == nombre_archivo:
                archivo_encontrado = archivo
                break
        if archivo_encontrado:
            archivo_encontrado.eliminar()
        else:
            print(f"No se encontró el archivo {nombre_archivo}")
    elif accion == "crear_directorio":
        nombre_directorio = partes[1]
        directorio_actual.crear_directorio(nombre_directorio)
    elif accion == "mover_archivo":
        nombre_archivo = partes[1]
        destino = partes[2]
       
        archivos = directorio_actual.listar_archivos()
        archivo_encontrado = None
        for archivo in archivos:
            if archivo.nombre == nombre_archivo:
                archivo_encontrado = archivo
                break
        if archivo_encontrado:
            directorio_destino = Directorio(destino)
            directorio_actual.mover_archivo(archivo_encontrado, directorio_destino)
        else:
            print(f"No se encontró el archivo {nombre_archivo}")
    elif accion == "generar_grafica":
        entidad = partes[1]
        generar_grafica(entidad)
    elif accion == "salir":
        print("Saliendo del chatbot...")
        exit()
    else:
        print("Comando no reconocido")
