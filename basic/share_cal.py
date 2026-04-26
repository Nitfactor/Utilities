def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Enter a real numeric number: TRY AGAIN")   

num_people = int(input("How many people are there ? "))
names = []

for i in range(num_people):
    name = input(f"Enter the name of the person #{i+1}").strip()
    names.append(name)

total_bill = get_float(("What is the total bill: "))
print("*" * 40)

share = round(total_bill / num_people)

print("*" * 40)
print(f"Total bill is {total_bill}")
print(f"Share for {share}")

for name in names:
    print(f"{name} owes {share} rupees")

print("\n" + "*" * 40)