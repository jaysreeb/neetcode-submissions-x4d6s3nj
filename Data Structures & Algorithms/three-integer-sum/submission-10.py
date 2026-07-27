class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            if num > 0:
                break
            if i > 0 and num == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l<r:
                sumOfthreenums = num +nums[l] + nums[r]
                if sumOfthreenums > 0:
                    r -= 1
                elif sumOfthreenums < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l <r:
                        l += 1
        return res
        # # sort the list
        # nums.sort()
        # # Initialize res as set/hash
        # res = set()
        # for i in range(len(nums)):
        #     # if the first element is greater than 0, it wouldnt add up to 0
        #     if nums[i] > 0:
        #         break
        #     # check if i>0
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue
        #     seen = set()
        #     for j in range(i + 1, len(nums)):
        #         complement = -nums[i] - nums[j]
        #         if complement in seen:
        #             # Add as tuples in the set res
        #             res.add((nums[i], complement, nums[j]))
        #         seen.add(nums[j])
        # return [list(t) for t in res]