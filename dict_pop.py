songs = {"Wannabe": 1, "Roar": 1, "Let It Be": 5, "Red Corvette": 4}

for s in songs.keys():
    if songs[s] == 1:
        songs.pop(s)