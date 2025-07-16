def find_max_min(list1):
    max=list1[0]
    min=list1[0]
    for ele in list1:
        if ele>max:
            max=ele
        if ele<min:
            min=ele
    return [max,min]

list1=list(map(int,input().split(',')))
a=find_max_min(list1)
print(f"max={a[0]},min={a[1]}")
