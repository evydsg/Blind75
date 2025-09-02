def threeSum(nums: List[int]) -> List[List[int]]:
    result = []
    nums = sorted(nums)

    for index in range(len(nums)):
        ptr1 = index + 1
        ptr2 = len(nums) -1 

        while ptr1 < ptr2 and index < ptr2:
            three_sum = nums[index] + nums[ptr1] + nums[ptr2]

            if three_sum < 0:
                ptr1 += 1
            elif three_sum > 0:
                ptr2 -= 1
            else:
                if [nums[index], nums[ptr1], nums[ptr2]] not in result:
                        result.append([nums[index], nums[ptr1], nums[ptr2]])
                ptr1 += 1
                ptr2 -= 1
        
    
    return result