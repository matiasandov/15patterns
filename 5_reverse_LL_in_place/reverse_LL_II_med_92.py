# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        0. left y right son posiciones indexadas en 1 no ints, por eso sabes hasta donde necesitas recorrer o parar con un for
        1. encuentra left y guardas si previo a left con un for
        2. revierte de left hasta right dejando un pointer 
        3. conectar los 3 tramos
        
        """
        dummy = ListNode(0, head)
        leftPrev = dummy
        curr = head
        #1. 
        for i in range(left-1):
            leftPrev = curr
            curr = curr.next
        #curr esta en posicion left (en el ejemplo solo hace 1 ciclo y avanza a nodo.val == 2)

        #2. revertir
        prev = None

        for i in range(right-left+1):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        #3.1 leftPrev apunta a left original que ahora es el final de la lista revertida. asi que ese final debe apuntar al tercer tramo
        #que ahora es curr
        leftPrev.next.next = curr
        # 3.2 ahora leftPrev debe apuntar al head de la lsita revertida que es prev
        leftPrev.next = prev

        return dummy.next
        
        
        




        