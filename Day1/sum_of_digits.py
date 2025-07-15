def sum_of_digits(n):
    sum=0
    while n>0:
        d=n%10
        sum+=d
        n=n//10
    return sum
n=int(input())
print(sum_of_digits(n))