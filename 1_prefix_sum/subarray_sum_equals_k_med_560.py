class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        1. el subarray es contiguos asi que podemos hacer prefix sum

        tal vez puedo agregar un extra zero al inicio y hacer todas las operaciones con index1 base o hacer un caso especifico para cuando
        tenga que sacar la suma entre i y j y i==0

        2. ahora debo sacar como todas las posibilidades de suma para contar cuantas son igual a k
        """
        
        #hay que anadir un caso base para 0
        #map de prefixsum y su count

        ps = {0:1}
        sum = 0
        countF = 0
        for i in range(len(nums)):
            sum += nums[i]

            #necesitamos este para lograr que nos de k
            diff_to_k = sum - k
            
            if diff_to_k in ps:
                countF += ps[sum - k]

            if sum not in ps:
                ps[sum] = 1
            else:
                ps[sum] += 1
       
    
        return countF
