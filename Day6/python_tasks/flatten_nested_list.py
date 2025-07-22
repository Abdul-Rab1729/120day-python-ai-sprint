def flatten_nested_list(list1):
    new_list=[]
    for i in range(len(list1)):
        new_list.extend(list1[i])
    return new_list

list1=[[1,2],[3,4],[5]]
print(flatten_nested_list(list1))