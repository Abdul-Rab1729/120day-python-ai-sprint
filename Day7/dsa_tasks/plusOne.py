def plusOne(digits):
      
    str1="".join(str(x) for x in digits)
    num=int(str1)+1
    return (list(map(int,(str(num)))))

digits=[1,2,3]
print(plusOne(digits))