def replace (d,v,e):
    for elem in d.keys():
        if(d[elem]==v):
            d[elem]=e
    print(d)


replace({1:2, 3:4, 4:2}, 2, 7)