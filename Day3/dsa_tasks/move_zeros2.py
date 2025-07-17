def move_zeros(list1):
    j=0
    for i in range(len(list1)):
        if list1[i]!=0:
            list1[i],list1[j]=list1[j],list1[i]
            j+=1
    return list1

list1=list(map(int,input().split(',')))
print(move_zeros(list1))