def str_to_int(s):
    res=0
    for ch in s:
        d=ord(ch)-ord('0')
        res=res*10+d
    return res