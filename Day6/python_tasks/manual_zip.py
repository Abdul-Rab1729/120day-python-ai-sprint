def manual_zip(list1,list2):
    for i in range(len(list1)):
        yield (list1[i],list2[i])
        i+=1

list1=[1,3,2,4,6]
list2=[1,2,5,6,7]
for i,j in manual_zip(list1,list2):
    print(i,j)