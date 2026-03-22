# Password Strength Checker & Suggestion Tool

import string
import getpass
import random

def pass_criteria(password):
    error = []
    if len(password) < 8:
        error.append("Too short")
    if not any(c.islower() for c in password):
        error.append("No character is in lowercase")
    if not any(c.isupper() for c in password):
        error.append("No character is uppercase")
    if not any(c.isdigit() for c in password):
        error.append("No character is a digit")
    if not any(c in string.punctuation for c in password):
        error.append("No punctuation found")
    return error

password = getpass.getpass("Enter a password: ")
print(password)
error = pass_criteria(password)

if not any(error):
    print("Your password is correct")
else:
    print("You have error in your password")
    for errors in error:
        print(f"- {error}")