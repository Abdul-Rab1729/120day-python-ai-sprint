def majority_element(list1):
    maj_ele=None
    count={}
    for x in list1:
        if x in count:
            count[x]+=1
        else:
            count[x]=1
    for x in list1:
        if count[x]>len(list1)//2:
            maj_ele=x
            break
    return maj_ele

list1=list(map(int,input().split(',')))
print(majority_element(list1))