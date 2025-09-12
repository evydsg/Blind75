class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        min_val = float("inf")

        while left <= right:
            middle = (left + right) // 2

            if nums[left] <= nums[middle]:
                if nums[left] <= nums[middle] <= nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if nums[left] >= nums[middle] >= nums[right]:
                    left = middle + 1
                else: 
                    right = middle - 1
            
            min_val = min(min_val, nums[middle])
        
        return min_val