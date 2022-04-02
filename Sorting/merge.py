


input_list = [3,7,5,1,4,8,2,9]

def merge(arr):
    if len(arr)<2:
        return
    array_lengh=len(arr)
    mid = array_lengh//2
    left_array=arr[:mid]
    right_array = arr[mid:]

    merge(left_array)
    merge(right_array)
    mergeSort(left_array,right_array,arr)
    


def mergeSort(L,R,arr):
    i=j=k=0
    while i<len(L) and j<len(R):
        if L[i]<=R[j]:
            arr[k]=L[i]
            i+=1
            k+=1
        else:
            arr[k]=R[j]
            j+=1
            k+=1

    while i<len(L):
        arr[k]=L[i]
        i+=1
        k+=1
    
    while j<len(R):
        arr[k]=R[j]
        j+=1
        k+=1

    

merge(input_list)
print(input_list)

