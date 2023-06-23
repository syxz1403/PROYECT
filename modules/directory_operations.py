import os

def renombrar_archivo(ruta_archivo, nuevo_nombre):
    
    directorio, nombre_archivo = os.path.split(ruta_archivo)

    nuevo_nombre_archivo = os.path.join(directorio, nuevo_nombre)

    try:
        os.rename(ruta_archivo, nuevo_nombre_archivo)
        print("Archivo renombrado exitosamente.")
    except OSError:
        print("Error al renombrar el archivo.")

ruta_archivo = "d:/PROYECT/tes.txt"
nuevo_nombre = "syxz"

renombrar_archivo(ruta_archivo, nuevo_nombre)

"""-----------------------------------------------------------------------------------------"""

def modificar_permisos(archivo, permisos):
    try:

        permisos_actuales = os.lstat(archivo).st_mode & 0o777

        nuevos_permisos = permisos_actuales | permisos

        os.chmod(archivo, nuevos_permisos)

        print(f"Se han modificado los permisos del archivo {archivo}")
    except FileNotFoundError:
        print(f"El archivo {archivo} no existe.")
    except:
        print("Ha ocurrido un error al intentar modificar los permisos.")

# Ejemplo de uso
archivo = "d:/PROYECT/2.2.txt"
permisos = 0o600  

modificar_permisos(archivo, permisos)
