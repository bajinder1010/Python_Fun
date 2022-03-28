def insertion_sort(unsorted_array):
    for i in range(0,len(unsorted_array)-1):
        j=i+1
        pile=unsorted_array[j]
        left_hand=unsorted_array[i]
        while(i>0 & left_hand>pile):
            if left_hand > pile:
                unsorted_array[i]=pile
                unsorted_array[j]=left_hand
            i-=1

    print(unsorted_array)



list=[1,4,2,3,5]

insertion_sort(list)


