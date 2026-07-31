class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        # Sorting would be O(nlogn)
        frequency = {}
        if len(s) != len(t):
            return False
        for char in s:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        for char in t:
            if char in frequency:
                frequency[char] -= 1
            else:
                return False
                
        for val in frequency.values():
            if val != 0:
                return False
        return True