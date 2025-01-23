#Crear una aplicación de consola en Python que permita a los usuarios gestionar sus tareas diarias
#añadir tareas con una descripcion y una fecha limite
#listar tareas (tareas pendientes, descripciones y fechas limites)
#marcar tarea como completada
#eliminar una tarea
#usar JSON
import json
from datetime import datetime

# Abre el archivo JSON en modo lectura
with open('tareas.json', 'r') as archivo:
    # Carga el contenido del archivo en un diccionario de Python
    tareas = json.load(archivo)

# Ahora `tareas` contiene los datos del archivo JSON

def add_task(tareas):
    task_name = input("Decime el nombre de la tarea que queres agregar: ").capitalize()
    task_description = input("Decime una descripcion de la tarea que queres agregar: ").capitalize()
    task_state = None
    task_date = None

    while task_state not in ["Completa","Pendiente"]:
        task_state = input("Decime si la tarea esta completa o no (Completa/Pendiente): ").capitalize()
        if task_state not in ["Completa","Pendiente"]:
            print("Entrada no válida., Por favor, ingrese una de las opciones disponibles.")

    while not task_date:
        fecha_limite = input("Decime cuando es la fecha limite de la tarea (DD/MM/AAAA): ")
        try:
            task_date = datetime.strptime(fecha_limite, "%d/%m/%Y")
            task_date = task_date.strftime("%d/%m/%Y")
        except ValueError:
            print("Fecha no válida. Por favor, usa el formato DD/MM/AAAA.")

    tareas[task_name] = {
        "descripcion": task_description,
        "completada": task_state,
        "fecha limite": task_date
    }

    return tareas

agregar = add_task(tareas)

with open("tareas.json","w") as archivo:
    json.dump(agregar,archivo,indent=4)



