# Challenge: CLI Contact Book (CSV-Powered)

# Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

# Your program should:
# 1. Ask the user to choose one of the following options:
#    - Add a new contact
#    - View all contacts
#    - Search for a contact by name
#    - Exit
# 2. Store contacts in a file called `contacts.csv` with columns:
#    - Name
#    - Phone
#    - Email
# 3. If the file doesn't exist, create it automatically.
# 4. Keep the interface clean and clear.

import os
import csv

filename = "contact.csv"
headers = [["Name", "Contact", "Email"]]

if not os.path.isfile(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def add_contact(name, contact, email):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, contact, email])
    print(f"Successfully added: {name}")

def load_options():
    pass

def search_contact():
    pass

def contact_book():
    while True:
        print("\nChoose one of the following\n")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact by name")
        print("4. Exit")

        choice = input("Select a number (1-4): ")

        match choice:
            case "1":
                name = input("Name: ")
                contact = input("Contact: ")
                email = input("Email: ")
                add_contact(name, contact, email)
            
            case "4":
                print("Exiting....")
                break
contact_book()


