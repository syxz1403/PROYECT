import os

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

