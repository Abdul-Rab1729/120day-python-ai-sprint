def longest_repeating_seq(s):
    max_cnt=float("-inf")
    c=''
    cnt=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cnt+=1
        if cnt>max_cnt:
            c=s[i]
        max_cnt=max(max_cnt,cnt)
        if s[i]!=s[i+1]:
            cnt=1
    return [c,max_cnt]

s="aaabbcccddddee"
print(longest_repeating_seq(s))