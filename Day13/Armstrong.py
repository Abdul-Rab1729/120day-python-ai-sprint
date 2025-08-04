def armstrong(n):
    temp=n
    res=0
    while temp>0:
        d=temp%10
        res+=d*d*d
        temp=temp//10
    return res==n

print(armstrong(153))
