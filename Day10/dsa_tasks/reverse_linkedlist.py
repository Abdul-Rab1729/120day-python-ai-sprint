class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
head=Node(0)
current=head

for i in range(1,6):
    current.next=Node(i)
    current=current.next




def reverse_linkedlist(head):
    prev=None
    curr=head
    while curr:
        new_node=curr.next
        curr.next=prev
        prev=curr
        curr=new_node
    return prev

rev_node=reverse_linkedlist(head)
while rev_node:
    print(rev_node.data, end="->")
    rev_node=rev_node.next
print("None")

