def longest_word(s):
    s=s.split()
    max_len=float("-inf")
    for x in s:
        max_len=max(max_len,len(x))
    for x in s:
        if len(x)==max_len:
            return x
    
s="If multiple have same length, return the first."
print(longest_word(s))