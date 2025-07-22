def long_unq_substring(s):
    
    max_cnt=0
    for j in range(len(s)):
        str1=""
        i=j
        while i<len(s) and s[i] not in str1:
            str1+=s[i]
            i+=1
        max_cnt=max(max_cnt,len(str1))
    return max_cnt   

s="abcabcbb"
print(long_unq_substring(s))