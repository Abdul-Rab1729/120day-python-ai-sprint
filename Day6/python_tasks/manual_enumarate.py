def manual_enumarate(nums,start=0):
    index = start
    for value in nums:
        yield (index, value)
        index += 1

list1=[1,3,2,4,6]
for i,v in manual_enumarate(list1):
    print(i,v)