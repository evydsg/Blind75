class Solution:
    def productExceptSelf(self, nums : List[int]) -> List[int]:
        prefix = postfix = 1
        prefix_arr = result = []
        postfix_arr = [1] * len(nums)

        for num in nums:
            prefix *= num
            prefix_arr.append(prefix)
        
        for index in range(len(nums) - 1, -1, -1):
            postfix *= nums[index]
            postfix_arr[index] = postfix
        
        for index in range(len(nums)):
            if index == 0:
                result.append(1 * postfix_arr[index + 1])
            else:
                if index == len(nums) - 1:
                    result.append(prefix_arr[index-1] * 1)
                else:
                    result.append(prefix_arr[index - 1] * postfix_arr[index + 1])
        
        return result