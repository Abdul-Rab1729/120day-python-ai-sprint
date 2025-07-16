def squares_list(n):
    list1=[]
    for i in range(1,n+1):
        list1.append(i*i)
    return list1

n=int(input())
print(squares_list(n))