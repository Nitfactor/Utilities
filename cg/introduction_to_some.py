import datetime

name = input("What is your name ?").strip()
age = input("What is your age ?").strip()
city = input("Which city do you live in ?").strip()
Profession = input("What profession are you in ?").strip()
hobby = input("What is your hobby ?").strip()

intro_message = (
    f"Hello, my name is {name}, I am {age} years old."
    f"I live in {city} and professionally I am a {Profession}."
    f"I love to {hobby} whenever I get a chance.\n"
)

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print(final_output)