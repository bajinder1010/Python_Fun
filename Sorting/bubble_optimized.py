list = [4,2,1,6,1,7,4,6,5]
not_sorted = True
while(not_sorted):
    not_sorted= False 
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
            temp= list[i]
            list[i]=list[i+1]
            list[i+1]=temp
            not_sorted= True 

print(list)    

