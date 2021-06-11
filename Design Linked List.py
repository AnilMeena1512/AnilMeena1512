class LinkedList:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
        
        

    def get(self, index) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index<0 or index >=self.size:
            return -1
        current=self.head
        for i in range(0,index):
            current=current.next
        return current.val
        

    def addAtHead(self, val) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.addAtIndex(0,val)
        

    def addAtTail(self, val) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.addAtIndex(self.size,val)
        

    def addAtIndex(self, index, val) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        current=self.head
        newNode=ListNode(val)
        if index<=0:
            newNode.next=current
            self.head=newNode
        else:
            for i in range(index-1):
                current=current.next
            newNode.next=current.next
            current.next=newNode
        self.size+=1
            
        

    def deleteAtIndex(self, index) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index<0 or index>=self.size:
            return
        current=self.head
        
        if index==0:
            self.head=self.head.next
        else:
            for i in range(index-1):
                current=current.next
            current.next=current.next.next
        self.size-=1
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
