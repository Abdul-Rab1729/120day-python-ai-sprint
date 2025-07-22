def long_unq_substr(s):
    start=0
    max_len=0
    str1=set()
    for i in range(len(s)):
        while s[i] in str1:
            str1.remove(s[start])
            start+=1
        str1.add(s[i])
        max_len=max(max_len,i-start+1)
    return max_len 

s="abcabcbb"
print(long_unq_substr(s))