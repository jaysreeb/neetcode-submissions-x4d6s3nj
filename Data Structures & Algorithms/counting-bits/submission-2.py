class Solution:
    def countBits(self, n: int) -> List[int]:
        # output = []
        # for i in range (n+1):
        #         count = 0
        #         while i != 0:
        #             rem = i % 2
        #             count += rem
        #             i = i // 2
        #         output.append(count)
        # return output
# Time Compelxity for the above is O(nlog n ) and space O(n)
        ans = [0] * (n+1)
        for i in range (1, n+1):
            ans[i] = ans[i >> 1] + (i &1)
        return ans
    # Time complexity is O(n) and space O(1)


        