def manual_sqrt(x):
    if x<2:
        return x
    left=1
    right=x//2
    while right>=left:
        mid=(left+right)//2
        sqr=mid*mid
        if sqr==x:
            return mid
        elif sqr<x:
            left=mid+1
        else:
            right=mid-1
    return right

print(manual_sqrt(64))
           