print("WORD FREQUENCY COUNTER")
sentence = input("Enter a sentence: ")
words = sentence.lower().split()
frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1
print("\nWORD FREQUENCY")
for word, count in frequency.items():
    print(word, ":", count)