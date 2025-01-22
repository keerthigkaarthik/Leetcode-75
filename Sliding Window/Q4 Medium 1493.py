# 1493. Longest Subarray of 1's After Deleting One Element
# Medium

# Given a binary array nums, you should delete one element from it.

# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

# Example 1:

# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

# Example 2:

# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

# Example 3:

# Input: nums = [1,1,1]
# Output: 2
# Explanation: You must delete one element.

 

# Constraints:

#     1 <= nums.length <= 105
#     nums[i] is either 0 or 1.




class Solution:
    # same solution as Sliding Window Q3
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
    def longestSubarray(self, nums: List[int]) -> int:
        return self.longestOnes(nums, 1) - 1