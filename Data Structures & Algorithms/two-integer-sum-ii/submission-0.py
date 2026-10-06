class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0 , len(numbers)-1

        while L < R:
            sum = numbers[L] +numbers[R]
            if  sum == target:
                return [L+1 , R+1]
            if sum < target:
                L = L +1
            elif sum > target:
                R = R - 1 
        return [L +1, R+1]
        