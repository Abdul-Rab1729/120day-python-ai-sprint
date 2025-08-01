def title_case_manually(s):
    list1=[]
    s1=s.split(" ")
    for x in s1:
        cap_x=chr(ord(x[0])-32)
        new_x=cap_x+x[1:len(x)]
        list1.append(new_x)
    return " ".join(list1)

s="hello world from python"
print(title_case_manually(s))