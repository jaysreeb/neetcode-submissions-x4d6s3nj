class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def search_recursive(nums: List[int], target: int, l: int, r: int) -> int:
            if l > r:
                return -1

            mid = l + ((r- l) // 2)

            if target == nums[mid]:
                return mid
            
            if target > nums[mid]:
                return search_recursive(nums, target, mid +1, r)
            else:
                return search_recursive(nums,target, l, mid -1)

        return search_recursive(nums, target, 0, len(nums) - 1)