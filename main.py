#Crear una aplicación de consola en Python que permita a los usuarios gestionar sus tareas diarias

import json
from datetime import datetime

archivo_tareas = "tareas.json"

with open('tareas.json', 'r') as archivo:
    tareas = json.load(archivo)

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
        "estado": task_state,
        "fecha limite": task_date
    }

    return tareas

agregar = add_task(tareas)

with open("tareas.json","w") as archivo:
    json.dump(agregar,archivo,indent=4)

def show_incomplete_task_in_archive(archivo_path):
    with open(archivo_path,"r") as archivo:
        tareas = json.load(archivo)
    
    for diccionario in tareas:
        if tareas[diccionario].get("estado") == "Pendiente":
            print(tareas[diccionario])
    return

def change_task_status(tareas):
    task_name_to_change_status = input("Decime el nombre de la tarea a la que le queres cambiar el estado de pendiente a completada: ").capitalize()

    if task_name_to_change_status in tareas:
        tareas[task_name_to_change_status]["estado"] = "Completa"
    
    return tareas

change_status = change_task_status(tareas)

with open("tareas.json","w") as archivo:
    json.dump(change_status,archivo,indent=4)

def delete_task_from_archive(tareas):
    task_to_delete = input("Decime el nombre de la tarea que queres eliminar: ").capitalize()

    if task_to_delete in tareas:
        del tareas[task_to_delete]
    return tareas

#delete_task = delete_task_from_archive(tareas)

#with open("tareas.json","w") as archivo:
    json.dump(delete_task,archivo,indent=4)
