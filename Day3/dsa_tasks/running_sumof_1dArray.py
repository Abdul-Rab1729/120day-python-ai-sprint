def runningSum( nums):
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        return nums
p=list(map(int,input().split(',')))
print(runningSum(nums=p))