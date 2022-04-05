def insertionSort(arr):
    for i in range(1,len(arr)):
        value = arr[i]
        hole= i
        while hole>0 and arr[hole-1]>value:
            arr[hole]=arr[hole-1]
            hole = hole-1
        
        arr[hole]=value

list_input =[2,4,1,3,8,2]

insertionSort(list_input)
print(list_input)