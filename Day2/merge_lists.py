def merge_lists(list1,list2):
    for ele in list2:
        list1.append(ele)
    return list1
list1=list(map(int,input().split(',')))
list2=list(map(int,input().split(',')))
print(merge_lists(list1,list2))