def rle_encode(s):
    new_str=""
    c=''
    cnt=1
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            cnt+=1
        if s[i]!=s[i+1]:
            c=s[i]
            new_str+=c+str(cnt)
            cnt=1
    c=s[i]
    new_str+=c+str(cnt)
    return new_str

s="aaabccddddd"
print(rle_encode(s))