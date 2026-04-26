import string

def pass_criteria(password):
    issues = []
    if len(password) < 8:
        issues.append("Must be min 8 characters")
    if not any(c.islower() for c in password):
        issues.append("No lowercase char found")
    if not any(c.isupper() for c in password):
        issues.append("No uppercase char found")
    if not any(c.isdigit() for c in password):
        issues.append("No digit found")
    if not any(c in string.punctuation for c in password):
        issues.append("No special char found")
    return issues
    

password = input("Your password: ")  
issues = pass_criteria(password)

if not issues:
    print("Your password is strong !")
    print(issues)
else:
    print("Your pass word is weak, create a strong password")
    print(issues)

