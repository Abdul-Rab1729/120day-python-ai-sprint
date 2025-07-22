def min_subarray(nums,k):
    start=0
    sum=0
    min_len=len(nums)+1

    for end in range(len(nums)):
        sum+=nums[end]
        while sum>=k:
            min_len=min(min_len,end-start+1)
            sum-=nums[start]
            start+=1
    return min_len if min_len<=len(nums) else 0