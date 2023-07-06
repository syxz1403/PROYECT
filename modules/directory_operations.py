
import os
import shutil
from modules.file_operations import Archivo

class Directorio:
    def __init__(self, ruta):
        self.ruta = ruta

    def listar_archivos(self):
        try:
            archivos = os.listdir(self.ruta)
            return [Archivo(archivo, os.path.join(self.ruta, archivo)) for archivo in archivos]
        except OSError as e:
            print(f"No se pudo listar los archivos en el directorio {self.ruta}: {e}")
            return []

    def crear_archivo(self, nombre):
        ruta = os.path.join(self.ruta, nombre)
        try:
            open(ruta, 'w').close()
            return Archivo(nombre, ruta)
        except OSError as e:
            print(f"No se pudo crear el archivo {nombre} en el directorio {self.ruta}: {e}")
            return None

    def crear_directorio(self, nombre):
        ruta = os.path.join(self.ruta, nombre)
        try:
            os.mkdir(ruta)
            return Directorio(ruta)
        except OSError as e:
            print(f"No se pudo crear el directorio {nombre} en el directorio {self.ruta}: {e}")
            return None

    def buscar_archivos(self, consulta):
        archivos = []
        try:
            for root, dirs, filenames in os.walk(self.ruta):
                for filename in filenames:
                    if consulta in filename:
                        ruta_archivo = os.path.join(root, filename)
                        archivos.append(Archivo(filename, ruta_archivo))
        except OSError as e:
            print(f"No se pudo buscar archivos en el directorio {self.ruta}: {e}")
        return archivos
    
    def mover_archivo(self, archivo, destino):
        try:
            shutil.move(archivo.ruta, os.path.join(destino.ruta, archivo.nombre))
            archivo.ruta = os.path.join(destino.ruta, archivo.nombre)
        except (shutil.Error, OSError) as e:
            print(f"No se pudo mover el archivo {archivo.nombre} al directorio {destino.ruta}: {e}")

