def right_rotate_list(nums,k):
    while k>0:
        temp=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            nums[i+1]=nums[i]
        nums[0]=temp
        k-=1
    return nums


nums=[1,2,3,4,5]
k=2
print(right_rotate_list(nums,k))