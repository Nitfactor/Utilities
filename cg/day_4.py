def convert(age):
    days = 365.25
    hours = 24
    minutes = 60

    total_days = age * days
    total_hours = total_days * hours
    total_minutes = total_hours * minutes

    return round(total_days), round(total_hours), round(total_minutes)

while True:
    try:
        your_age = float(input("What is your age: "))
        your_days, your_hours, your_minutes = convert(your_age)

        print("\n You are approx:")
        print(f"  -  {your_days} days old")
        print(f"  -  {your_hours} hours old")
        print(f"  -  {your_minutes} minutes old\n")

        again = input("Would you like to try again: (y/n)").strip().lower()

        if again != 'y':
            print("Good bye")
            break
    except:
        print("Please enter a valid number for age !")