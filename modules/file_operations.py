import os

"""-----------------------------------------------------------------------------------------"""
""""PERMISOS
Permiso de lectura: 100 (binario) / 4 (octal)
Permiso de escritura: 010 (binario) / 2 (octal)
Permiso de ejecución: 001 (binario) / 1 (octal)

Lectura y escritura para el propietario, sin permisos para el grupo y otros: 110 000 000 (binario) / 600 (octal)
Lectura, escritura y ejecución para el propietario, lectura y ejecución para el grupo y otros: 111 101 101 (binario) / 755 (octal)
Lectura y ejecución para el propietario y grupo, sin permisos para otros: 110 101 000 (binario) / 550 (octal)
"""

class Archivo:
    def __init__(self, nombre, ruta):
        self.nombre = nombre
        self.ruta = ruta

    def renombrar(self, nuevo_nombre):
        nueva_ruta = os.path.join(os.path.dirname(self.ruta), nuevo_nombre)
        try:
            os.rename(self.ruta, nueva_ruta)
            self.nombre = nuevo_nombre
            self.ruta = nueva_ruta
        except OSError as e:
            print(f"No se pudo renombrar el archivo {self.nombre}: {e}")

    def eliminar(self):
        try:
            os.remove(self.ruta)
        except OSError as e:
            print(f"No se pudo eliminar el archivo {self.nombre}: {e}")

    def cambiar_permisos(self, permisos):
        try:
            os.chmod(self.ruta, permisos)
        except OSError as e:
            print(f"No se pudieron cambiar los permisos del archivo {self.nombre}: {e}")
