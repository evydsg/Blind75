class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequency = [[] for index in range(len(nums)+1)]
        result = []
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for key, value in count.items():
            frequency[value].append(key)
        
        for index in range(len(frequency) - 1, -1, -1):
            for num in frequency[index]:
                result.append(num)

                if len(result) == k:
                    return result