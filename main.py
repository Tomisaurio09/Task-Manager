# Create a console application in Python that allows users to manage their daily tasks

import json
from datetime import datetime

tasks_file = "tasks.json"
# Sequence of try and except in case of any error with the JSON file
try:
    with open(tasks_file, 'r') as file:
        tasks = json.load(file)
except FileNotFoundError:
    print(f"Error: The file '{tasks_file}' is not found.")
    tasks = {}
except json.JSONDecodeError:
    print(f"Error: The file '{tasks_file}' contains invalid JSON data.")
    tasks = {}
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
    tasks = {}

# Essential function to validate all types of inputs
def validate_input(message, options):
    validated_task = None
    while validated_task not in options:
        validated_task = input(message).capitalize()
        if validated_task not in options:
            print("Invalid input. Please, enter one of the available options.")
    return validated_task

# Allows adding tasks to the JSON file
def add_task(tasks):
    task_name = input("Tell me the name of the task you want to add: ").capitalize()
    task_description = input("Tell me a description of the task you want to add: ").capitalize()
    task_state = validate_input("Tell me if the task is complete or not (Complete/Pending): ", ["Complete", "Pending"])
    task_date = None

    while not task_date:
        deadline = input("Tell me the deadline of the task (DD/MM/YYYY): ")
        try:
            task_date = datetime.strptime(deadline, "%d/%m/%Y")
            task_date = task_date.strftime("%d/%m/%Y")
        except ValueError:
            print("Invalid date. Please, use the format DD/MM/YYYY.")
            print("An example of a valid date would be: 05/09/2006")

    tasks[task_name] = {
        "description": task_description,
        "state": task_state,
        "deadline": task_date
    }

    return tasks

# Shows the user the pending tasks to be done
def show_incomplete_tasks_in_archive(file_path):
    try:
        with open(file_path, "r") as file:
            tasks = json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' is not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON data.")
        return
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
        return
    if tasks:
        for task in tasks:
            if tasks[task].get("state") == "Pending":
                print(tasks[task])
    else:
        print("There are no pending tasks in the file")
    return

# Allows the user to change the status of a task to complete after completing it
def change_task_status(tasks):
    task_name_to_change_status = input("Tell me the name of the task you want to change from pending to complete: ").capitalize()

    if task_name_to_change_status in tasks:
        tasks[task_name_to_change_status]["state"] = "Complete"
        print(f"The task named '{task_name_to_change_status}' has successfully changed from 'Pending' to 'Complete'")
    else:
        print(f"The task '{task_name_to_change_status}' does not exist")
        user_choice = validate_input("Do you want to change the status of another task? (Y/N): ", ["Y", "N"])
        if user_choice == "N":
            print("Thank you for using my program")
            exit()
        elif user_choice == "S":
            change_task_status(tasks)
    
    return tasks

# Allows the user to delete any task as long as it exists in the JSON file
def delete_task_from_archive(tasks):
    task_to_delete = input("Tell me the name of the task you want to delete: ").capitalize()

    if task_to_delete in tasks:
        del tasks[task_to_delete]
        print(f"The task named '{task_to_delete}', was successfully deleted")
    else:
        print(f"The task '{task_to_delete}' does not exist")
        user_choice = validate_input("Do you want to delete another task? (Y/N): ", ["Y", "N"])
        if user_choice == "N":
            print("Thank you for using my program")
            exit()
        elif user_choice == "S":
            delete_task_from_archive(tasks)

    return tasks

# Simple introduction to the program
def introduction():
    print("Hello User!\n")
    print("This is a simple Task Manager.")
    print("You can add a task, delete them, you can check their status and you can change their status.")

# Interactive menu that allows the user to choose what to do with their tasks
def main():
    introduction()

    print("\nWhat do you want to do?")
    print("""
        1. Add a Task
        2. Delete a Task
        3. Check the incomplete tasks
        4. Change the task status
        5. Exit the program
            """)
    
    user_choice = validate_input("Choose one of the available options: ", ["1", "2", "3", "4", "5"])

    if user_choice == "1":
        added = add_task(tasks)
        try:
            with open(tasks_file, "w") as file:
                json.dump(added, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

    elif user_choice == "2":
        deleted = delete_task_from_archive(tasks)
        try:
            with open(tasks_file, "w") as file:
                json.dump(deleted, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

    elif user_choice == "3":
        show_incomplete_tasks_in_archive(tasks_file)

    elif user_choice == "4":
        changed_status = change_task_status(tasks)
        try:
            with open(tasks_file, "w") as file:
                json.dump(changed_status, file, indent=4)
        except Exception as e:
            print(f"An unexpected error occurred while writing to the file: {e}")

    elif user_choice == "5":
        print("Thank you for using my Task Manager")
        exit()

main()
