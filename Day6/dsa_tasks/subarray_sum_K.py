def subarray_sum_k(nums,k):
    i,j=0,0
    sum=0
    list1=[]
    while i<len(nums):
        sum+=nums[i]
        while sum>k:
            sum-=nums[j]
            j+=1
        if sum==k:
            list1.append(nums[j:i+1])
        i+=1
    return list1