import os

TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if (os.path.exists(TASK_FILE)):
        with open(TASK_FILE, "r", encoding="UTF-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks

def task_manager():
    tasks = load_tasks()

    while True:
        print("\n------Task List Manager -------")
        print("1. Add task")
        print("2. View Tasks")
        print("3. Mark Task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5)").strip()
