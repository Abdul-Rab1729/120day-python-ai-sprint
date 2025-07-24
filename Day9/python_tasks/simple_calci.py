class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b if a>b else b-a
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return round(a/b,2) if b>0 else print("Error: Divided by 0")
    
calci=Calculator()
print(calci.add(2,3))
print(calci.subtract(1,9))
print(calci.multiply(1,4))
print(calci.divide(2,3))
print(calci.divide(2,0))
    