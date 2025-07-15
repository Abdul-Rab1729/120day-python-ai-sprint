def reverse_string(strr):
    n=len(strr)
    new_strr=""
    for i in range(n-1,-1,-1):
        new_strr+=strr[i]
    return new_strr

def palindrome_check(strr):
    if reverse_string(strr)==strr:
        return True
    else:
        return False
strr=input()
print(palindrome_check(strr.lower()))    