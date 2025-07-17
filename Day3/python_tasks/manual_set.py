def manual_set(list1):
    set_like_list=[]
    for x in list1:
        if x not in set_like_list:
            set_like_list.append(x)
    return sorted(set_like_list)
list1=list(map(int,input().split(',')))
print(manual_set(list1))