def read_root():
    Name = input("Name:")
    Contact = input("Contact:")
    Age = input("Age:")
    return(f"Name:{Name}\nContact:{Contact}\nAge:{Age}")

Account_Created = read_root()

with open("db.txt", "a") as file:
    file.write(Account_Created)