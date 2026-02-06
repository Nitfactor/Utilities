import datetime

journal = input("Your learning: ")

now = datetime.datetime.now()

journal_entry = (f"{now} \n {journal}")

with open("Learning.txt", "a", encoding="utf-8") as f:
    f.write(journal_entry)

print(f"\n your journal entry has been saved to 'Learning.txt")