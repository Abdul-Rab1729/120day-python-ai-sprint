def second_largest(nums):
    largest=float('-inf')
    sec_largest=float('-inf')
    for i in range(len(nums)):
        if nums[i]>largest:
            sec_largest=largest
            largest=nums[i]
        elif nums[i]>sec_largest and nums[i]<largest:
            sec_largest=nums[i]
    if sec_largest==float('-inf'):
        return None
    return sec_largest