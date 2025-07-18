def max_sum_subarray(nums, k, target):
    n = len(nums)
    if n < k:
        return []
    window_sum = sum(nums[:k])
    if window_sum == target:
        return nums[:k]
    for i in range(k, n):
        window_sum = window_sum - nums[i - k] + nums[i]
        if window_sum == target:
            return nums[i - k + 1 : i + 1]
    return []
