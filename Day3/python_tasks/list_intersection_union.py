def lists_intersection(list1,list2):
    new_list=[]
    for x in list1:
        if x in list2:
            new_list.append(x)
    return sorted(new_list)

def lists_union(list1,list2):
    for x in list2:
        if x not in list1:
            list1.append(x)
    return sorted(list1)

list1=list(map(int,input().split(',')))
list2=list(map(int,input().split(',')))
print("Intersection_of_Lists:",lists_intersection(list1,list2))
print("Union_of_Lists:",lists_union(list1,list2))
