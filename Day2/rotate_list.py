def right_rotate_list(list1,k):
    n=len(list1)
    new_list=list1[n-k:n]+list1[0:n-k]
    return new_list
def left_rotate_list(list1,k):
    n=len(list1)
    new_list=list1[k:n]+list1[0:k]
    return new_list
list1=list(map(int,input().split(',')))
k=int(input())
print(right_rotate_list(list1,k))
print(left_rotate_list(list1,k))