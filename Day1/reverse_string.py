def reverse_string(strr):
    n=len(strr)
    new_strr=""
    for i in range(n-1,-1,-1):
        new_strr+=strr[i]
    return new_strr

strr=input()
print(reverse_string(strr))