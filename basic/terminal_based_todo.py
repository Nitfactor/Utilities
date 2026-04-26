import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if (os.path.exists(TASK_FILE)):
        with open(TASK_FILE, 'r', encoding = "utf-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks

def save_task(tasks):
    with open(TASK_FILE, 'w', encoding="utf-8") as f:
        for task in tasks:
            status = "done" if task["done"] else "not done"
            f.write(f"{task['text']}||{status}\n")

def display_tasks(tasks):
    if not tasks:
        print(f"NO tasks found")
    else:
        for i, task in enumerate(tasks, 1):
            checkbox = "✅" if task["done"] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

def task_manager():
    tasks = load_tasks()

    while True:
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option(1-5): ")

        match choice:
            case "1":
                text = input("Enter your task: ").strip()
                if text:
                    tasks.append({"text": text, "done": False})
                    save_task(tasks)
                else:
                    print("Task cannot be empty") 

            case "2":
                display_tasks(tasks)

            case "3":
                display_tasks(tasks)
                try:
                    num = int(input("Enter the task number: "))
                    if 1 <= num <= len(tasks):
                        tasks[num-1]["done"] = True
                        save_task(tasks)
                        print("Tasks marked done")
                    else:
                        print("Invalid")    
                except ValueError:
                    print("Enter a valid number")

            case "4":
                display_tasks(tasks)           
                try:
                    num = int(input("Enter task number: "))
                    if 1 <= num <= len(tasks):
                        remove = tasks.pop(num-1)
                        save_task(tasks)
                        print(f"Task removed: {remove["text"]}")
                    else:
                        print("Invalid number")
                except ValueError:
                    print("Enter a valid number")

            case "5":
                print("Exit task manager")
                break

            case _:
                print("Please choose a valid option")

task_manager()