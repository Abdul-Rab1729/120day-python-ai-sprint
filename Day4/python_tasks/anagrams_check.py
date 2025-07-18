def check_anagrams(s1,s2):
    dict1,dict2={},{}
    for ch in s1:
        if ch in dict1:
            dict1[ch]+=1
        else:
            dict1[ch]=1
    for ch in s2:
        if ch in dict2:
            dict2[ch]+=1
        else:
            dict2[ch]=1
    return dict1==dict2
s1=input()
s2=input()
print(check_anagrams(s1,s2))