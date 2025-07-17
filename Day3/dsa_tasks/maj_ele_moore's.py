def maj_ele(list1):
    candidate=None
    count = 0
    for x in list1:
        if count == 0:
            candidate = x
        if x == candidate:
            count += 1
        else:
            count -= 1
    cnt=0
    for x in list1:
        if x==candidate:
            cnt+=1
    if cnt>len(list1)//2:
        return candidate 
    else:
        return None


list1=list(map(int,input().split(',')))
print(maj_ele(list1))