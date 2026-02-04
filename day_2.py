import textwrap

Name = input("Write your name ").strip()
Age = input("Write your Age ").strip()
Profession = input("Write your Profession ").strip()
Emoji = input("Give your favourite emoji ").strip()

print("What style do you want ?" \
"1. Horizontal with your favourite emoji border.\n" \
"2. Vertical with your favourite emoji border \n" \
"3. Minimalist design \n" \
"4. Professional design\n")
Style = input("Choose your style among: 1, 2, 3, 4 ")

def chosen_style(style):
    if style == "1":
        return f"{Emoji*30} \n Hello, my name is {Name}, I am {Age} years old and my profession is {Profession} \n {Emoji*30}"
    elif style == "2":
        return f"{Emoji*30} \n {Emoji*30} \n Hello, my name is {Name}, I am {Age} years old and my profession is {Profession} \n {Emoji*30}"
    elif style == "3":
        return f"Hello, my name is {Name}, I am {Age} years old and my profession is {Profession}"
    elif style == "4":
        return f"Hello, my name is {Name}, I am {Age} years old and my profession is {Profession} \n {Emoji*30}"

bio = chosen_style(Style)

print("\n Your stylish bio\n")
print("*" * 50)
print(textwrap.dedent(bio))
print("*" * 50)

save = input("Do you want to save the your style in a text file ? (y/n)").lower()

if save == 'y':
    filename = f"{Name.lower().replace(" ","_")}_bio.txt"
    with open(filename, "w" , encoding="utf-8") as f:
        f.write(bio)
    print("File saved successfully")