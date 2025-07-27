def single_num(nums):
    xor=0
    for n in nums:
        xor^=n
    return xor

nums=[1,2,1,2,4]
print(single_num(nums))