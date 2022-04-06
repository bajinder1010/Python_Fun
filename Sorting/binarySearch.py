def BSearch(arr,num):
    start = 0
    end = len(arr)-1
   
    while start<=end:
        mid = (start+end)//2
        if num == arr[mid]:
            return True

        elif num < mid:
            
            end=mid-1
        else:
            start = mid+1
            

    return False

list_input = [1,2,3,4,5]
result = BSearch(list_input,6)
print(result)



