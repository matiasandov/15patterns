# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        necesitas guardar 
        prev
        cur 
        next


        
        """
        dummy = ListNode(0,head)
        curr = head
        prev = dummy

        while curr is not None and curr.next  is not None :
            next = curr.next
            #1.prev apunta al que se va a intercambiar
            prev.next = next
            #2. curr apuntas al sig PAIR 
            curr.next = next.next
            #3. intercambias de lugar 
            next.next = curr
            #4.avanzas al sig par
            prev = curr
            curr = curr.next
            

        return dummy.next

            
            

            


        