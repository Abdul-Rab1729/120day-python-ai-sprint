class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node('A')
node2=Node('B')
node3=Node('C')
node4=Node('D')
node5=Node('E')
node6=Node('F')
node7=Node('G')
node8=Node('H')

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8
node8.next=node3

head=node1

def detect_cycle_start(head):
    slow=fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next

        if slow==fast:
            break
    
    slow=head
    while slow!=fast:
        slow=slow.next   
        fast=fast.next
    print("Cycle Start at node with value:",slow.data)
    return slow

print(detect_cycle_start(head))
