def min_subarray(nums,k):
    list1=[]
    for i in range(len(nums)):
        sum=0
        j=i
        while sum<k and j<len(nums):
            sum+=nums[j]
            j+=1
        if sum>=k:
            list1.append(nums[i:j])
    print(list1)

    if len(list1)==0:
        return 0
    
    min_len=len(nums)
    for x in list1:
        if len(x)<min_len:
            min_len=len(x)
    
    return min_len

nums=[2,3,1,2,4,3]
k=7
print(min_subarray(nums,k))