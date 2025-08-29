class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        frequency_sort = dict(sorted(frequency.items(), key = lambda item: item[1], reverse = True))

        
        for key in frequency_sort:
            result.append(key)
            k -= 1

            if k == 0:
                break

        
        return result
        
