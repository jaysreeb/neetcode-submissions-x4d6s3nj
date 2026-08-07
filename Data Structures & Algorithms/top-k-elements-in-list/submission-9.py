class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #    Keep count of numbers appearing in nums using a dictionary count
        count ={} 
        for num in nums:
            count[num] =count.get(num, 0) + 1
        heap = []
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        # arr = []
        # for num, cnt in count.items():
        #     arr.append([cnt, num])
        # arr.sort()

        # res = []
        # while len(res) < k:
        #     res.append(arr.pop() [1])
        # return res
