def factorial_recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial_recursion(n-1)

def factorial_loop(n):
    res=1
    for i in range(n,1,-1):
        res*=i
    return res

n=int(input())
print(factorial_loop(n))
print(factorial_recursion(n+1))