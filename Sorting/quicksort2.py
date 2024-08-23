def quicksort(arr):
    if len(arr) <= 1 :
        return arr

    smaller =[]
    equal =[]
    larger=[]

    pivot = arr[-1]

    for num in arr:
        if num<pivot :
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)

    return quicksort(smaller) + equal + quicksort(larger)

arr = [1,3,2,5,7,2]
print(quicksort(arr))
