def read_text (filename):
    """
    filename: string, name of the file to read
    returns: string,contains all the file content
    """
    inFile = open(filename,'r')
    line = inFile.read()
    return line



import string
def find_words(text):
    """
    text: string
    return: list of words from input text
    """
    text= text.replace("\n"," ")
    for char in string.punctuation:
        text = text.replace(char,"")
    words = text.split(" ")
    return words




def frequencies(words):
    """
    words: list of words
    returns: frequency dictionary for input words
    """
    freq_dict ={}

    for word in words:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1
    return freq_dict





def calculate_similarity(dict1, dict2):
    """
    dict1: frequency dictionary for one text
    dict2: frequency dictionary for another text
    returns: float, representing how similar both text are to each other
    """
    diff=0
    total =0

    for word in dict1.keys():
        if word in dict2.keys():
            diff += abs(dict1[word]-dict2[word])
        else:
            diff += dict1[word]

    for word  in dict2.keys():
        if word not in dict1.keys():
            diff +=dict2[word]
    
    total = sum(dict1.values())+ sum(dict2.values())
    difference= diff/total
    similar = 1.0 - difference
    
    return round(similar,2)


text_1 = read_text("bob.txt") 
text_2 = read_text("bobb.txt") 
words_1 = find_words(text_1) 
words_2 = find_words(text_2) 
freq_dict_1 = frequencies(words_1)
freq_dict_2 = frequencies(words_2) 
print(calculate_similarity(freq_dict_1, freq_dict_2))