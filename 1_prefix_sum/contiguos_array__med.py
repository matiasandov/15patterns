class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        

        """
        Description:
        Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

        Example 1:

        Input: nums = [0,1]
        Output: 2
        Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
        Example 2:

        Input: nums = [0,1,0]
        Output: 2
        Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
        Example 3:

        Input: nums = [0,1,1,1,1,1,0,0,0]
        Output: 6
        Explanation: [1,1,1,0,0,0] is the longest contiguous subarray with equal number of 0 and 1.
        

        Constraints:

        1 <= nums.length <= 105
        nums[i] is either 0 or 1.
        
        
        Problem solving
        O n**2 if i wanted to check all the subarrays
            any solution I achieve should be better than this

        a. first thought dict 
        b. i feel like this could be more of a sliding window problem - > not gonna work!bc there is no way to know if i should move to the right or left
        c. there should be a linear O n solution
        
        Solution: removing a minimun prefix and checking for balance
        1. usaremos un dict
        2. vamos a manejarlo de manera que el prefix tenga un 1 para tener un extra 1
            zeros = 2 , ones = 3 
        3. asi podremos remover ese prefix y no preocuparnos por los zoeros

        4. en el dict pondremos la diferencia entre zeros y unos para cada index donde el index sera el prefijo de un array completo

        
        """
        # [ diferencia de ones : index del ulitmo elemento del subarray]
        dif_ones ={}
        ones = 0
        zeros = 0
        res = 0

        #1. fill dict
        for i in range(0,len(nums)):

            if nums[i] == 0:
                zeros += 1
            else:
                ones += 1
            
            #mapea difference para despues quitar el prefix desde su index 
            if ones - zeros not in dif_ones:
                dif_ones[ones - zeros] = i
            
            if ones == zeros:
                #length total - this not gonna be the longest one always
                res = ones + zeros
            else:
                idx = dif_ones[ones-zeros]
                res = max(res, i-idx)
        return res

    
