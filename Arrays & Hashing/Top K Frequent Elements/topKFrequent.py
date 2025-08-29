class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []

        for num in nums:
            if num in frequency:
                frequency[num] -= 1
            else:
                frequency[num] = -1
        
        heap = [(value, key) for key, value in frequency.items()]
        heapq.heapify(heap)

        while heap:
            value, key = heapq.heappop(heap)
            result.append(key)

            k -= 1
            if k == 0:
                break

        return result