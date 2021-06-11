# Definition for singly-linked list.
#class ListNode:
#def __init__(self, x):
#self.val = x
#self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen_val=set()
        current=head
        while current!=0:
            if current in seen_val:
                return True
            seen_val.add(current)
            current=current.next
        return False
