def long_con_seq(nums):
    
    max_len=0
    i=0
    while i<len(nums):
        list1=[]
        k=nums[i]
        while k in nums:
            list1.append(k)
            k+=1
        
        max_len=max(len(list1),max_len)
        i+=1
    return max_len


nums=[0,3,7,2,5,8,4,6,0,1]
print(long_con_seq(nums))