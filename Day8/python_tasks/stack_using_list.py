class stack_using_list():
    def __init__(self):
        self.list1=[]
        self.cnt=0
    def pop(self):
        self.cnt-=1
        return self.list1.pop()
    
    def push(self,x):
        self.list1.append(x)
        self.cnt+=1
    def top(self):
        return self.list1[self.cnt-1]
    def is_empty(self):
        if self.cnt==0:
            return True
        else:
            return False
    def display(self):
        for i in range(self.cnt):
            print(self.list1[i], end=" ")


list1=stack_using_list()
print(list1.is_empty())
list1.push(2)
list1.push(3)
list1.push(5)
list1.push(4)
list1.push(6)
print(list1.pop())
print(list1.top())
print(list1.display())
    