#Ask the user for 5 numbers.
#Store them in a list.
#Print the largest number.

# Numbers = float(input("Write 5 numbers"))
# Num = []

# for i in range(Numbers):
#     Number = input(f"Write your numbers {i+1}, ").strip()
#     Num.append(Number)

# largest = max(Numbers)

# if Numbers < 5:
#     print("Numbers are less than 5: TRY AGAIN")
# print(f"Largest number given by you is {largest}")


Num = []

for i in range(5):
    Number = float(input(f"Five numbers {i+1}: "))
    Num.append(Number)

largest = max(Num)

print(f"Largest number given by you is {largest} ")