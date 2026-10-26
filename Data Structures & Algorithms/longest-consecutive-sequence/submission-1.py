class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest_streak = 0
        
        for num in numsSet:
            if (num -1) not in numsSet:
                current_num = num
                current_streak = 1
                while (num+current_streak) in numsSet:
                    current_streak += 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak







