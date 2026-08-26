class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Declaring a dictionary to carry the key value pairs
        result = {}
        # Looping through nums using enumerate to keep index and values
        for i, num in enumerate(nums):
            # We need to find the difference in the hash map if exist and add if doesnt
            diff = target - num
            if diff in result:
                return [result[diff], i]
            result[num] = i
        # if the array is empty or if there is no pair 
        return []
            




        