import os
from modules.file_operations import Archivo
from modules.directory_operations import Directorio
from chats.chart_generation import generar_grafica
from modules.natural_language_procesing import Nlp

respuesta_bot = ""

def chatbot():
    os.chdir("D:\PROYECT")  
    directorio_actual = Directorio(os.getcwd())  
    nlp = Nlp(directorio_actual, "data/preprocessing.ipynb/data_processed.csv")
    nlp.initialize_nlp()

    while True:
        command = input("Ingrese un comando: ")

        if command.lower() == "exit":
            break

        response = nlp.response(command)
        print(response)

if __name__ == "__main__":
    chatbot()
