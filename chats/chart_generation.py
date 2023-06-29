import matplotlib.pyplot as plt
import csv


def generar_grafica(entidad):
    
    try:
        datos_entidad = []
        
        with open("data_processed.csv", "r") as archivo_csv:
            lector_csv = csv.DictReader(archivo_csv)
            
            for fila in lector_csv:
                if fila["nit_de_la_entidad"] == entidad:
                    datos_entidad.append(fila)
        
        fechas = []
        montos = []
        for dato in datos_entidad:
            fechas.append(dato["fecha"])
            montos.append(float(dato["monto_contratacion"]))
        
        plt.plot(fechas, montos)
        plt.xlabel("Fecha")
        plt.ylabel("Monto de contratación")
        plt.title(f"Datos históricos de contratación para la entidad {entidad}")
        plt.show()
        
    except FileNotFoundError:
        print("No se encontró el archivo de datos")
    except Exception as e:
        print(f"No se pudo generar la gráfica: {e}")


