# Definition for singly-linked list.
#class ListNode:
#def __init__(self, x):
#self.val = x
#self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        ##Two pointer approach
        slower=faster=head
        while slower and faster and faster.next:
            slower=slower.next
            faster=faster.next.next
            if slower==faster:
                return True
        return False
