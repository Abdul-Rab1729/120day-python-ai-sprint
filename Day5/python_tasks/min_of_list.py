def min_of_list(list1):
    min=list1[0]
    for x in list1:
        if min>x:
            min=x
    return min

list1=input().split(',')
print(min_of_list(list1))