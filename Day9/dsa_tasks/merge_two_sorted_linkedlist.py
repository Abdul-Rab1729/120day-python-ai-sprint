class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None

n=6
head1=Node(0)
head2=Node(1)
nums1=head1
nums2=head2
for i in range(2,n):
    if i%2==0:
        nums1.next=Node(i)
        nums1=nums1.next
    else:
        nums2.next=Node(i)
        nums2=nums2.next

def merge_sorted_lists(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    if l1.data<l2.data:
        head=l1
        l1=l1.next
    else:
        head=l2
        l2=l2.next

    current=head

    while l1 and l2:
        if l1.data<l2.data:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next
    current.next=l1 if l1 else l2
    return head

merged=merge_sorted_lists(head1,head2)

while merged:
    print(merged.data, end="->")
    merged=merged.next
print("None")

        