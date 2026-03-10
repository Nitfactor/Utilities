# The first function is used when the input must be an integer, if not then the system breaks.
# There were two instances when we needed an integer and in both the places we used the function.

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("TRY AGAIN")

num_people = int(input("How many people are there ? "))
name = []

for i in range(num_people):
    names = input(f"Enter the name of each person {i+1} : ")
    name.append(names)
# here the function is used to get a integer value !
total_bill = get_float("What is the total bill: ")

share = (total_bill / num_people)

print("*" * 40)
print(f"Total bill is {total_bill}.")
print(f"Share of each person comes out to be {share}.")

for name in names:
    print(f"{name} will share {share} rupees")

print("*" * 40)

