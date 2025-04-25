#O (n+m)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = {}
        stack = []
        
        for i in range(len(nums2)):
            while stack and nums2[i] > nums2[stack[-1]]:
                digit = nums2[stack.pop()]
                res[digit] = nums2[i]
            stack.append(i)
        
        #los que sobraron sin greater value
        for idx in stack:
            res[nums2[idx]] = -1
        
        new = []

        for i in range(len(nums1)):
            if nums1[i] in res:
                new.append(res[nums1[i]])

        return new

        