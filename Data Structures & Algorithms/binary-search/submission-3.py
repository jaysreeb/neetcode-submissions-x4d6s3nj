class Solution:
    def binary_search(self, nums: List[int], target: int, l:int, r:int) -> int:
        if l >  r:
            return -1
        mid = l + ((r -l) //2)

        if target == nums[mid]:
            return mid

        if nums[mid] < target:
            return self.binary_search(nums, target, mid +1, r)
        else:
            return self.binary_search(nums, target, l, mid - 1)
            
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)