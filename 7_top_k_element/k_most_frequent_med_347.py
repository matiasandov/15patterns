class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #1. count freq dict
        #2. push (-freq, value) to heap y asi se ordena el heap de menor a mayor por su freq
        # al agregar el signo negativo, los k primeros seran los k mas frecuentes
        # 3. haz k veces pop() al heap y quedate con el value
        freq = {}
        #1
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        #2.
        heap = []
        heapq.heapify(heap)
        for key,v in freq.items():
            heapq.heappush( heap, (-v, key))

        res = []
        #3.
        for i in range(0,k):
            a = heapq.heappop(heap)
            res.append(a[1])
        return res

        
        

        
            

        