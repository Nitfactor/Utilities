sentence = input("Write your sentence").lower()
words = sentence.split()
filler_words = ["the", "is", "a", "an", "and", "to", "in" ]
filtered_words = []

for word in words:
    if word not in filler_words:
        filtered_words.append(word)

updated_sentence = " ".join(filtered_words)

print("\nUpdated Sentence: \n")
print(updated_sentence)