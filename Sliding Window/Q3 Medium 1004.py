# 1004. Max Consecutive Ones III
# Medium

# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# Example 2:

# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

 

# Constraints:

#     1 <= nums.length <= 105
#     nums[i] is either 0 or 1.
#     0 <= k <= nums.length



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        p1 = 0
        p2 = 0
        curr_k = k
        max_n = 0
        while p2 < len(nums):
            if nums[p2] == 1:
                p2 += 1
            else:
                if curr_k != 0:
                    p2 += 1
                    curr_k -= 1
                else:
                    if nums[p1] == 0:
                        p2 += 1
                        p1 += 1
                    else:
                        max_n = max(max_n, p2-p1)
                        while nums[p1] != 0:
                            p1 += 1
                        p1 += 1
                        p2 += 1
        max_n = max(max_n, p2-p1)
        return max_n