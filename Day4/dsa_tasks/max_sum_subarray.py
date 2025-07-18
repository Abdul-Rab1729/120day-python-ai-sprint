def max_sum_subarray(nums,k,target):
    i,j=0,0
    while i<=len(nums)-k:
        list1=[]
        sum,cnt=0,0
        j=i
        while cnt<k:
            sum+=nums[j]
            list1.append(nums[j])
            j+=1
            cnt+=1
        if sum==target:
            return list1
        i+=1
    return []