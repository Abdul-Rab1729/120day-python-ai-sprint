def camelcase_to_snakecase(s):
    new_str=''
    for i in range(len(s)):
        if ord(s[i]) in range(65,91): 
            new_str+='_'+chr(ord(s[i])+32)
            continue
        new_str+=s[i]
    return new_str

s='myVariableName'
print(camelcase_to_snakecase(s))