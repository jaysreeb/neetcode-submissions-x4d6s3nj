class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT ={}, {}

        for count in s:
            countS[count] = countS.get(count,0) + 1 
        for count in t:
            countT[count] = countT.get(count, 0) +1

        return countS == countT