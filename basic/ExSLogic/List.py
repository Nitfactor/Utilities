list = ["a", "e", "i", "o", "u"]

answer = input("Write the vowels in English language: ").lower().split()

if answer == list:
    print("Correct")
else:
    print("Incorrect")