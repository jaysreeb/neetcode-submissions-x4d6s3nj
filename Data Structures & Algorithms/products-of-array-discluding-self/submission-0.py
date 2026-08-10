class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_products = [1] * n
        right_products = [1] * n

        output = [1] * n
        # building the prefix
        #  Fill the left products (forward loop)
        for i in range(1, n):
            left_products[i] = left_products[i-1] * nums[i-1]
        
        # building the suffix
        # Fill the right products (backward loop)
        for i in range(n-2, -1, -1):
            right_products[i] = right_products[ i+1] * nums[i+1]

        for i in range(n):
            output[i] = left_products[i] * right_products[i]

        return output
