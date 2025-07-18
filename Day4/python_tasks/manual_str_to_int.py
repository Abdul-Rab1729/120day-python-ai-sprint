def manual_str_to_int(s):
    result=0
    for ch in s:
        result=result*10+ord(ch)-ord('0')
    return result

s=input()
print(manual_str_to_int(s))
print(type(manual_str_to_int(s)))