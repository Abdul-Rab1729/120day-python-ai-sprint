def char_frequency(strr):
    freq={}
    for char in strr:
        if char in freq:
            freq[char]+=1
        else:
            freq[char]=1
    return freq
strr=input()
print(char_frequency(strr))