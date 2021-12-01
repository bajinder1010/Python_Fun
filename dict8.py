def invert(d):
    d_inv ={}
    list =[]
    for key in d.keys():
        if d[key] not in d_inv:
            d_inv[d[key]]=[key]
        else:
            d_inv[d[key]].append(key)
    print(d_inv)


invert({1:1, 3:1, 5:1})