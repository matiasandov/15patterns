class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        """
        case a: a single number smaller than k is consider to be one subrray

        1. go sliding the window from the left if prod  >= k 
        2. update count by:
            - each new element to the subarray is a subarray itself so (+1)
            - each element of the array represents a combination of subarrays (r-beg)

        """

        count = 0
        prod = 1
        beg = 0
        
        for r in range(len(nums)):

            prod *= nums[r]
            #move the left pointer (beg) til prod < k
            #1.
            while beg <= r and prod >= k:
                #eliminas del prod el primer elemento del subarray y checas si se excede o no 
                prod = prod // nums[beg]
                beg += 1
            #2.
            count += r-beg+1
        return count



