class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
str1="madam"
head=Node('m')
current=head
for ch in str1[1:]:
    current.next=Node(ch)
    current=current.next
"""def traversal(head):
    current=head
    while current:
        print(current.data, end="->")
        current=current.next
traversal(head)"""
def linkedlist_palindrome(head):

    def middle_node(head):
        slow=fast=head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

    middle=middle_node(head)

    prev=None
    curr=middle
    while curr:
        next_node=curr.next
        curr.next=prev
        prev=curr
        curr=next_node

    first=head
    second=prev

    while second:
        if first.data!=second.data:
            return False
        first=first.next
        second=second.next
    return True

print(linkedlist_palindrome(head))