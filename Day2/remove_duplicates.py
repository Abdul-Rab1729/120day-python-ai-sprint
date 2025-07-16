def remove_duplicates(list1):
    list2=[]
    for ele in list1:
        if ele not in list2:
            list2.append(ele)
    return list2

list1=map(int,input().split(","))
print(remove_duplicates(list1))
