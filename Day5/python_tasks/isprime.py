def isprime(n):
    if n==0 or n==1:
        return False
    count=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            count+=1
    if count>0:
        return False
    else:
        return True 

n=int(input())
print(isprime(n))