def most_frequent(nums):
    count={}
    for x in nums:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    max_freq=0
    most_common=None
    for key in count:
        if count[key]>max_freq:
            max_freq=count[key]
            most_common=key
    return most_common
nums=[1,1,2,3,4,4,4,5]
print(most_frequent(nums))