def evl_postfix_exp(s):
    stack=[]
    for i in range(len(s)):
        if s[i]==" ":
            continue
        if s[i]=='+':
            right=stack.pop()
            left=stack.pop()
            stack.append(left+right)
            continue
        if s[i]=='-':
            right=stack.pop()
            left=stack.pop()
            stack.append(left-right)
            continue
        if s[i]=='*':
            right=stack.pop()
            left=stack.pop()
            stack.append(left*right)
            continue
        if s[i]=='/':
            right=stack.pop()
            left=stack.pop()
            stack.append(left/right)  
            continue
        stack.append(int(s[i]))  
        
    return stack[0]

s="3 4 + 2 *"
print(evl_postfix_exp(s))