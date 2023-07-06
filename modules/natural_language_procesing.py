import random
import string
import warnings
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from modules.file_operations import Archivo
from modules.directory_operations import Directorio
from chats.chart_generation import generar_grafica

class Nlp:
    def __init__(self, directorio, ruta_corpus):
        self.sent_tokens = []
        self.GREETING_INPUTS = ("hola", "saludos", "qué tal", "hey", "¿cómo estás?")
        self.GREETING_RESPONSES = ["¡Hola!", "¡Hola! ¿En qué puedo ayudarte?", "*asiente*", "Hola, ¿en qué puedo ayudarte?", "Hola, me alegra que estés chateando conmigo"]
        self.BOT_NAME = "Dil-Bot"
        self.directorio = directorio
        self.ruta_corpus = ruta_corpus

    def initialize_nlp(self):
        warnings.filterwarnings('ignore')
        nltk.download('popular', quiet=True)
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)

        with open(self.ruta_corpus, 'r', encoding='utf8', errors='ignore') as fin:
            texto = fin.read().lower()

        self.sent_tokens = nltk.sent_tokenize(texto)

    def lem_tokens(self, tokens):
        lematizador = WordNetLemmatizer()
        return [lematizador.lemmatize(token) for token in tokens]

    def lem_normalize(self, texto):
        remove_punct_dict = dict((ord(puntuacion), None) for puntuacion in string.punctuation)
        return self.lem_tokens(nltk.word_tokenize(texto.lower().translate(remove_punct_dict)))

    def greeting(self, oracion):
        for palabra in oracion.split():
            if palabra.lower() in self.GREETING_INPUTS:
                return random.choice(self.GREETING_RESPONSES)

    def response(self, respuesta_usuario):
        respuesta_bot = ''
        self.sent_tokens.append(respuesta_usuario)
        TfidfVec = TfidfVectorizer(tokenizer=self.lem_normalize, stop_words='english')
        tfidf = TfidfVec.fit_transform(self.sent_tokens)
        vals = cosine_similarity(tfidf[-1], tfidf)
        idx = vals.argsort()[0][-2]
        flat = vals.flatten()
        flat.sort()

        if flat[-2] == 0:
            respuesta_bot = respuesta_bot + "Lo siento, pero no estoy seguro de lo que estás preguntando."
            return respuesta_bot

        if self.greeting(respuesta_usuario) is not None:
            respuesta_bot = respuesta_bot + self.greeting(respuesta_usuario) + ". ¿En qué puedo ayudarte hoy?"
            return respuesta_bot

        comando = respuesta_usuario.lower()

        if "generando gráfica" in comando or "generar gráfica" in comando:
            entidad = input("Por favor, ingresa el nombre de la entidad: ")
            generar_grafica(entidad)
            respuesta_bot = respuesta_bot + "Gráfica generada exitosamente."

        elif "buscar archivo" in comando:
            nombre_archivo = input("Por favor, ingresa el nombre del archivo que deseas buscar: ")
            archivos = self.directorio.buscar_archivos(nombre_archivo)
            if archivos:
                respuesta_bot = respuesta_bot + "Archivos encontrados:\n"
                for archivo in archivos:
                    respuesta_bot = respuesta_bot + archivo.nombre + "\n"
            else:
        
                respuesta_bot = respuesta_bot + "No se encontraron archivos con ese nombre."

        elif "crear archivo" in comando:
            nombre_archivo = input("Por favor, ingresa el nombre del nuevo archivo: ")
            nuevo_archivo = self.directorio.crear_archivo(nombre_archivo)
            if nuevo_archivo:
                respuesta_bot = respuesta_bot + "Archivo creado exitosamente."
            else:
                respuesta_bot = respuesta_bot + "No se pudo crear el archivo."

        elif "eliminar archivo" in comando:
            nombre_archivo = input("Por favor, ingresa el nombre del archivo que deseas eliminar: ")
            archivo_eliminar = self.directorio.buscar_archivos(nombre_archivo)
            if archivo_eliminar:
                archivo_eliminar[0].eliminar()
                respuesta_bot = respuesta_bot + "Archivo eliminado exitosamente."
            else:
                respuesta_bot = respuesta_bot + "No se encontró el archivo."

        elif "renombrar archivo" in comando:
            nombres = input("Por favor, ingresa el nombre actual y el nuevo nombre del archivo separados por coma: ")
            nombre_actual, nuevo_nombre = nombres.split(",")
            archivo_renombrar = self.directorio.buscar_archivos(nombre_actual.strip())
            if archivo_renombrar:
                archivo_renombrar[0].renombrar(nuevo_nombre.strip())
                respuesta_bot = respuesta_bot + "Archivo renombrado exitosamente."
            else:
                respuesta_bot = respuesta_bot + "No se encontró el archivo."

        elif "mover archivo" in comando:
            nombres = input("Por favor, ingresa el nombre del archivo que deseas mover y la ruta de destino separados por coma: ")
            nombre_archivo, ruta_destino = nombres.split(",")
            archivo_mover = self.directorio.buscar_archivos(nombre_archivo.strip())
            directorio_destino = Directorio(ruta_destino.strip())
            if archivo_mover and directorio_destino:
                self.directorio.mover_archivo(archivo_mover[0], directorio_destino)
                respuesta_bot = respuesta_bot + "Archivo movido exitosamente."
            else:
                respuesta_bot = respuesta_bot + "No se pudo mover el archivo."
             
        elif "salir" in comando:
                respuesta_bot = respuesta_bot + "¡Hasta luego!"
                # Aquí puedes agregar cualquier otra acción o lógica que desees realizar antes de salir del programa.
                exit()
        else:
                respuesta_bot = respuesta_bot + "No entiendo ese comando. Por favor, intenta de nuevo."

        self.sent_tokens.remove(respuesta_usuario)
        return respuesta_bot