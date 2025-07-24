class queue_using_list():
    def __init__(self):
        self.list1=[]
        self.front=0
        self.rear=0

    def enqueue(self,x):
        self.list1.append(x)
        self.rear+=1

    def dequeue(self):
        self.rear-=1
        self.list1.remove(self.list1[self.front])

    def top(self):
        return self.list1[self.front]
    
    def is_empty(self):
        if len(self.list1)==0:
            return True
        else:
            return False
    
    def display(self):
        for i in range(self.rear):
            print(self.list1[i], end=" ")

q=queue_using_list()
print(q.is_empty())
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.dequeue()
q.enqueue(7)
print(q.top())
q.display()

    
      