def add_word(d,word,defination):
    if word in d:
        d[word].append(defination)
    else:
        d[word] = [defination]


words={}
add_word(words,'box','fight')
print(words)
add_word(words, 'box', 'container')
print(words)
add_word(words, 'ox', 'animal')
print(words)
