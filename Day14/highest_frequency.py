import collections
def highest_frequency(nums):
    freq=collections.Counter(nums)
    return freq.most_common(1)
nums=[1,1,2,2,2,3,4]
print(highest_frequency(nums))