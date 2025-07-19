def list_to_string(list1):
    str1=""
    for x in list1:
        str1+=x
    return str1

list1=input().split(' ')
print(list_to_string(list1))