# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a=l1 #pointers
        b=l2 #pointers
        
        array_1=[]
        array_2=[]
        
        while a.next is not None:
            array_1.append(a.val)
            a=a.next
        array_1.append(a.val)
        
        
        while b.next is not None:
            array_2.append(b.val)
            b=b.next
        array_2.append(b.val)
        
        #print(array_1)
        #print(array_2)
        
        array_1.reverse()
        array_2.reverse()
        
        inta=int("".join(str(x) for x in array_1)) #converting list to strings
        intb=int("".join(str(x) for x in array_2))
        
        #print(inta)
        #print(intb)

        
        sum_str=list(str(inta+intb)) #add two integer strings and convert sum into list
        
        
        head=l3=ListNode(sum_str.pop()) #Initialize the head of l3 with the las element of sum_str list
        
        sum_str.reverse()
        
        #traverse remaining digits,and assign each of them in new LIstNode
        for i in sum_str:
            l3.next=ListNode(i)
            l3=l3.next
        return head
