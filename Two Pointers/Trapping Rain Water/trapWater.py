class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        max_water = 0
        left_max = height[left]
        right_max = height[right]

        while left < right:
            if left_max > right_max:
                right -= 1
                right_max = max(height[right], right_max)
                water_trapped = right_max - height[right]
                max_water += water_trapped
            else:
                left += 1
                left_max = max(height[left], left_max)
                water_trapped = left_max - height[left]
                max_water += water_trapped
        
        return max_water