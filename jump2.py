nums =[2,3,1,1,4]

left =0
right=0
maxReach =0
minJumps =0

while right < len(nums)-1:
    for i in range (left,right+1):
        maxReach= max(maxReach,nums[i]+i)
    left = right + 1
    right = maxReach
    minJumps+=1

print(minJumps)
