from modules.file_operations import Archivo
from modules.directory_operations import Directorio
from modules.natural_language_procesing import procesar_comando
from chats.chart_generation import generar_grafica
import os

def chatbot():
    os.chdir("D:\PROYECT")  
    directorio_actual = Directorio(os.getcwd())  
    while True:
        command = input("Ingrese un comando: ")
        procesar_comando(command, directorio_actual)  

if __name__ == "__main__":
    chatbot()