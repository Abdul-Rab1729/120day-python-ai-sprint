def sum_divisible_by_k(nums,k):
    count = 0
    n = len(nums)

    for start in range(n):
        total = 0
        for end in range(start, n):
            total += nums[end]
            if total % k == 0:
                count += 1

    return count

nums = [4,5,0,-2,-3,1]
k = 5
print(sum_divisible_by_k(nums,k))