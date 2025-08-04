def first_non_repeat_char(s):
    s = s.lower()
    
    for i in range(len(s)):
        is_unique = True
        for j in range(len(s)):
            if i != j and s[i] == s[j]:
                is_unique = False
                break
        if is_unique:
            return s[i]
    
    return None 
        
    

s="endevour"
print(first_non_repeat_char(s))