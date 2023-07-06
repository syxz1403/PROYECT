import matplotlib.pyplot as plt
import csv
from modules.file_operations import Archivo
from modules.directory_operations import Directorio




def generar_grafica(entidad):
    
    try:
        datos_entidad = []
        
        with open("data/preprocessing.ipynb/data_processed.csv", "r") as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            
            for fila in lector_csv:
                if fila["nit_de_la_entidad"] == entidad:
                    datos_entidad.append(fila)
        
        fechas = []
        montos = []
        for dato in datos_entidad:
            fechas.append(dato["fecha_firma_yyymm"])
            montos.append(float(dato["valor_contrato"]))
        
        plt.plot(fechas, montos)
        plt.xlabel("fecha")
        plt.ylabel("valor contrato")
        plt.title(f"Datos históricos de contratación para la entidad {entidad}")
        plt.show()
        
    except FileNotFoundError:
        print("No se encontró el archivo de datos")
    except Exception as e:
        print(f"No se pudo generar la gráfica: {e}")


"""def procesar_comando(comando, directorio_actual):
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
        print("Comando no reconocido")"""
