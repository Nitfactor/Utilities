get_emoji = {
    "love": "❤️" ,
    "happy": "☺️",
    "sad": "😔",
}

message = input("Write your message: ")

updated_words = []

for words in message.split():
    cleaned = words.lower().strip(",!?/")
    emoji = get_emoji.get(cleaned, "")

    if emoji:
        updated_words.append(f"{words} {emoji}")
    else:
        updated_words.append(words)

updated_message = " ".join(updated_words)
print("\n Enhanced message:\n")
print(updated_message)