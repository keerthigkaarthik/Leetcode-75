# 643. Maximum Average Subarray I
# Easy

# You are given an integer array nums consisting of n elements, and an integer k.

# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

# Example 1:

# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

# Example 2:

# Input: nums = [5], k = 1
# Output: 5.00000

 

# Constraints:

#     n == nums.length
#     1 <= k <= n <= 105
#     -104 <= nums[i] <= 104



class Solution(object):
    def findMaxAverage(self, nums, k):
        if k == 1:
            return max(nums)
        max_sum = nums[0]
        for i in range(1, k):
            max_sum += nums[i]
        sum = max_sum
        for i in range(k, len(nums)):
            sum = sum + nums[i] - nums[i-k]
            max_sum = max(sum, max_sum)
        print(max_sum/k)
        return max_sum/k
