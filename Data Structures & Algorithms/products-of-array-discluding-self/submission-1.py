class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        prefix_output = [] # declaring a list prefix_output
        for i in range(n):
            prefix_output.append(prefix)
            prefix = prefix * nums[i]

        suffix = 1
        suffix_output = []
        for i in range(n-1, -1, -1):
            prefix_output[i] *= suffix
            suffix *= nums[i]
        
        return prefix_output
        
