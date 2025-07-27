class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(1)
node1 = Node(2)
node2 = Node(2)
node3 = Node(4)
node4 = Node(5)
node5 = Node(5)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def remove_dup(head):
    current = head
    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next
    return head

ans = remove_dup(head)
while ans:
    print(ans.data, end="->")
    ans = ans.next
print("None")
