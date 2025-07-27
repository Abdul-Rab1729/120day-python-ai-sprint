def int_to_bin(n):
    bin=""
    while n>0:
        rem=n%2
        bin=str(rem)+bin
        n=n//2
    return bin        

print((int_to_bin(16)))