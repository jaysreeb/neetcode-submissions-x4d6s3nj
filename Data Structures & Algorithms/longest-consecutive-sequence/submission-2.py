class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak =0
        set_nums = set(nums)

        for num in set_nums:
            if (num-1) not in set_nums:
                current_streak = 1                
                while (num + current_streak) in set_nums:
                    current_streak += 1
                longest_streak = max(current_streak, longest_streak)
        return longest_streak

        