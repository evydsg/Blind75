class Solution:
    def hasDuplicates(self, nums: List[int]) -> bool:
        dict_nums = {}

        for num in nums:
            if num in dict_nums:
                dict_nums[num] += 1
                return True
            
            dict_nums[num] = 1
        
        return False