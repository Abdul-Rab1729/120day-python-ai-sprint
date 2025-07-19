def count_subarray(nums, target):
    i = 0  
    j = 0  
    sum = 0
    max_len = 0
    result = []

    while i < len(nums):
        sum += nums[i]
        while sum > target:  
            sum -= nums[j]
            j += 1
        if sum == target:
            result.append(nums[j:i+1])
        i += 1
    return len(result)
