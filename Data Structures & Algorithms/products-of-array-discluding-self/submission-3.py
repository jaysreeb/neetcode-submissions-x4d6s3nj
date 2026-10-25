class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prefix = 1     
        n = len(nums)
        for i in range(n):
            result.append(prefix)
            prefix = prefix * nums[i]        
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]          
        
        return result

        