# 283. Move Zeroes
# Easy

# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

 

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:

# Input: nums = [0]
# Output: [0]

 

# Constraints:

#     1 <= nums.length <= 104
#     -231 <= nums[i] <= 231 - 1

 
# Follow up: Could you minimize the total number of operations done?



class Solution(object):
    def moveZeroes(self, nums):
        p1 = 0
        p2 = len(nums)-1
        while p1 < p2:
            if nums[p1] != 0:
                p1 += 1
            elif nums[p2] == 0:
                p2 -= 1
            else:
                current_p1 = p1
                while current_p1 < p2:
                    temp = nums[current_p1 + 1]
                    nums[current_p1 + 1] = 0
                    nums[current_p1] = temp
                    current_p1 += 1
        