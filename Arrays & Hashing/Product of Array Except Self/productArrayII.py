class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = postfix = 1
        result = []

        for nums in nums:
            result.append(prefix)
            prefix *= nums
        
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= postfix
            postfix *= nums[index]
        
        return result
