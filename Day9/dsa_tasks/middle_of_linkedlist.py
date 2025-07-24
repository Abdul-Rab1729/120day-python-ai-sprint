class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=4
head=Node(0)
node=head
for i in range(1,n):
    node.next=Node(i)
    node=node.next

def middle_of_linkedlist(head):
    slow=fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    return slow.data

print(middle_of_linkedlist(head))