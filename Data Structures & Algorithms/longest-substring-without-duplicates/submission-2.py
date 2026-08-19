class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores character -> last seen index
        left = 0
        max_length = 0
    
        for right, char in enumerate(s):
        # If character is in window, jump left pointer forward
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
        # Record/update the character's position
            char_map[char] = right
        
        # Calculate current window size and update max
            max_length = max(max_length, right - left + 1)
        
        return max_length

