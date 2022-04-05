def quickSort(arr,start,end):
    if start < end:

        pIndex= getPindex(arr,start,end)
        quickSort(arr,start,pIndex-1)
        quickSort(arr,pIndex+1,end)


def getPindex(arr,start,end):

    pivot = arr[end]
    pIndex = start
     
    for i in range(start,end):

        if arr[i]<=pivot:
            temp = arr[i]
            arr[i]=arr[pIndex]
            arr[pIndex]=temp
            pIndex+=1
    
    temp2 = arr[pIndex]
    arr[pIndex]=arr[end]
    arr[end]=temp2
    return pIndex

list_input = [6,2,1,4]
quickSort(list_input,0,len(list_input)-1)
print(list_input)
