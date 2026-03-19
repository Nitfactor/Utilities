import os

TASK_FILE = "tasks.txt"

def load_tasks():
    pass

def display_tasks(tasks):
    pass





def task_manager():
    tasks = load_tasks()

    while True:
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose among the 1-5 : ")

        match choice:
            case "1":
                text = input("Enter your task").strip()
                if text:
                    tasks.append({"text":text, "done":False})
                    save_tasks(tasks)
                else:
                    print("Tasks cannot be empty")

            case "2":
                display_tasks(tasks)
            
            case "3":
                display_tasks(tasks)

