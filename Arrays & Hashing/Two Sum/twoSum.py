class Solution:
    def two_sum(self, nums: List[int], target) -> int:
        prev_hash = {}

        for index, num in enumerate (nums):
            difference = target - num

            if difference in prev_hash:
                return [prev_hash[difference], index]
            
            prev_hash[num] = index