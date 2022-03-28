list =[9,7,8,4,2,3,1]

for j in range(0,len(list)):
    for i in range(0,len(list)-1):
        if list[i]>list[i+1]:
           temp = list[i]
           list[i]=list[i+1]
           list[i+1]= temp
           
print(list)
    


