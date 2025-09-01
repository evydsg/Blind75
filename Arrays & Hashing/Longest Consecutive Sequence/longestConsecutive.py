class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums = set(nums) #convert to set to ensure it does not have duplicates

        for num in nums:
            start = num
            
            if num - 1 in nums:
                start = num - 1
            
            sequence = 1

            while start + 1 in nums:
                sequence += 1
                start = start + 1
            
            longest = max(longest, sequence)
        
        return longest