class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = defaultdict(int)

        # for num in nums:
        #     count[num] += 1
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)
    # Step 4: Gather the top k frequent elements from right to left
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        

