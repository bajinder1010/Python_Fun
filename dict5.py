lyrics = "Happy birthday to you Happy birthday to you Happy birthday dear Happy birthday to you" 
counts = {}
words = lyrics.split(" ")
print(words)
for word in words:
    word = word.lower()
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1
print(counts)
