def twosum(nums, target):
        i = 0
        j = i + 1
        while i < len(nums) - 1:
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i, j]
                j += 1
            i += 1
            j = i + 1  
        return [] 

nums=list(map(int,input().split(',')))
target=int(input())
print(twosum(nums,target)) 
        