words ="""ink
oil
pen
wax
clay
draw
film
crosshatching
"""
tiles = "hijklmnop"
all_valid_words = ()
start=0
end=0
found_words=()
for char in words:
    if char == "\n":
      #print(all_valid_words)  
      all_valid_words = all_valid_words + (words[start:end],)
      start= end + 1
      end = end +1
    else:
      end = end+1
print(all_valid_words)

for word in all_valid_words:
    tiles_left = tiles
    #print(tiles_left)
    for letter in word:
        if letter not in tiles_left:
            break
        else:
            index = tiles_left.find(letter)
            #print(index)
            tiles_left = tiles_left[:index]+tiles_left[index+1:]
            #print(tiles_left)
    if len(word)==len(tiles)-len(tiles_left):
        found_words = found_words + (word,)

print(found_words)



      

    