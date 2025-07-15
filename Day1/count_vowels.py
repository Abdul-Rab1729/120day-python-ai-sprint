def count_vowels(strr):
    vowels={'a':False,'e':False,'i':False,'o':False,'u':False}
    cnt=0
    for char in strr:
        if char in vowels and vowels[char]==False:
            cnt+=1
            vowels[char]=True
    return cnt

strr=input()
print(count_vowels(strr.lower()))