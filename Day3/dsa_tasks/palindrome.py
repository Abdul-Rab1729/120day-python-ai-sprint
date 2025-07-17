
def isPalindrome( x):
        if x<0:
            return False
        if 0<=x<10:
            return True
        r=0
        n=x
        while n>0:
            r=r*10+n%10
            n=n//10
        return r==x
x=int(input())
print(isPalindrome(x))