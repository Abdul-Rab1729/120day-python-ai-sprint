def twosum(nums,target):
    dict1={}
    for i in range(len(nums)):
        diff=target-nums[i]
        if diff in dict1:
            return [dict1[diff],i]
        dict1[nums[i]]=i
    return []

nums=list(map(int,input().split(',')))
target=int(input())
print(twosum(nums,target)) 