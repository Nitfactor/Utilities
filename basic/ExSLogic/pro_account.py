import json
import os


def account_creation():
    Name = input("Name: ")
    Contact = input("Contact: ")
    Age = input("Age: ")
    return {"name": Name, "contact": Contact, "age": Age}

def save_to_storage(data, path="storage.json"):

    all_records = []
    
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "r", encoding="utf-8") as f:
            try:
                all_records = json.load(f)

                if not isinstance(all_records, list):
                    all_records = [all_records]
            except json.JSONDecodeError:

                all_records = []

    all_records.append(data)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_records, f, indent=4)
    
    print(f"Entry saved successfully to {path}!")


account_created = account_creation()
save_to_storage(account_created)
