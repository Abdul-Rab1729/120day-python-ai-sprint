def sort_012(list1):
    low,mid,high=0,0,len(list1)-1
    while mid<=high:
        if list1[mid]==0:
            list1[low],list1[mid]=list1[mid],list1[low]
            low+=1
            mid+=1
        elif list1[mid]==1:
            mid+=1
        elif list1[mid]==2:
            list1[high],list1[mid]=list1[mid],list1[high]
            high-=1
    return list1

list1=[1,1,0,0,2,1]
print(sort_012(list1))
