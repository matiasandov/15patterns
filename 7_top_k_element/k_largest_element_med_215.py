#usando quick select parecido a qucksort
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #1. tomas los primeros k elementos digamos que nums = [3,2,1,5,6,4], k = 2
        # entonces heap = [2,3] -> el smallest quedara hasta arriba en heap[0]
        heap = nums[:k]
        heapq.heapify(heap)

        """
        2. se itera en los que sobran [1,5,6,4] y comparas contra cada elemento en el heap 
        la idea es ir haciendo swap hasta que en el heap queden los k mas grandes
        """
        for n in nums[k:]:
            if n > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, n)

        #el smallest del heap quedara en [0]
        return heap[0]




#mejor respuesta!!








#esta fue la que me dio mejor tiempo, pero siento que es lo mismo que ordenar
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = len(nums) -k

        heapq.heapify(nums)

        for i in range(res):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)
    

#usando minheap esta si la acepta
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        res = heapq.nlargest(k,nums)
        return res[-1]


#esta no la acepta leetcode pero es la mas interesante porque usas quickselect

#usando quick select parecido a quickselect
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        convertir en un grafo ordenado a partir de un head node random head = 
        1. partirlo en dos eligiendo un nodo random como head del grafo -> el average time complexity es O(n), el peor es O(n**2)
            1.1 por practicidad siempre se esta eligiendo el ultimo elemento del array
        2. - si tu k es mayor que el index de head, sabes que tienes que ordenar la segunda mitad del array nada mas, con quick sort
            - si tu k es menor que el index de head, sabes que solo tienes que ordenar la primera mitad
        3, ya que esta ordenado solo debes tomar el index lenghth-k
        """

        k = len(nums) -k

        def quickselect(l,r):
            #siempre se usara el ultimo
            head = nums[r]
            #pointer que recorrera hasta la primera mitad que sea menor a head
            p = l
            #excluye el ultimo
            for i in range(l,r):
                #si el valor actual es mas chico que head, lo mandas a la primera mitad y se va ordenado con el swap
                if nums[i] <= head:
                    nums[i], nums[p] = nums[p], nums[i]
                    #avanzas en la primera mitad
                    p += 1
            
            #intercambia head a la mitad del array que es donde se quedo p
            nums[p], nums[r] = head, nums[p]

            #se  k es menor a p, ordenas en la primera mitad
            if p > k:
                return quickselect(l, p-1)
            elif p < k:
                return quickselect(p+1, r)
            else:
                return nums[p]
        return quickselect(0, len(nums)-1)

