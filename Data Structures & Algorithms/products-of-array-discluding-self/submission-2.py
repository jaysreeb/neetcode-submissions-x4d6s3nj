class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        result = []
        for i in range(n):
            result.append(prefix)
            prefix = prefix * nums[i]

        suffix = 1
        suffix_output = []
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
        
