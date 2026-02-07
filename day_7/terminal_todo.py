import os

TASK_FILE = "tasks.txt"

def load_task():
    tasks = []
    if (os.path.exists(TASK_FILE)):
        with open(TASK_FILE, "r", encoding="UTF-8") as f:
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text": text, "done": status == "done"})
    return tasks

    