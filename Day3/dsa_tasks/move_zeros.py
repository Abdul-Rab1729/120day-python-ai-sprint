def move_zeros(list1):
    zeros=[]
    non_zeros=[]
    for x in list1:
        if x!=0:
            non_zeros.append(x)
        else:
            zeros.append(x)
    return non_zeros+zeros

list1=list(map(int,input().split(',')))
print(move_zeros(list1))