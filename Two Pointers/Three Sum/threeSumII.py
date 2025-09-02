class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            ptr2, ptr3 = index + 1, len(nums) - 1

            while ptr2 < ptr3:
                three_sum = value + nums[ptr2] + nums[ptr3]

                if three_sum < 0:
                    ptr2 += 1
                elif three_sum > 0:
                    ptr3 -= 1
                else:
                    result.append([value, nums[ptr2], nums[ptr3]])
                    ptr2 += 1
                    ptr3 -= 1

                    while ptr2 < ptr3 and nums[ptr2] == nums[ptr2 - 1]:
                        ptr2 += 1
                    while ptr2 < ptr3 and nums[ptr3] == nums[ptr3 + 1]:
                        ptr3 -= 1

        return result
