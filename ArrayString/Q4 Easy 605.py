# 605. Can Place Flowers
# Easy

# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.



# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true

# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false

 

# Constraints:

#     1 <= flowerbed.length <= 2 * 104
#     flowerbed[i] is 0 or 1.
#     There are no two adjacent flowers in flowerbed.
#     0 <= n <= flowerbed.length



class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        if n == 0:
            return True
        l = len(flowerbed)
        if l < 2:
            return l != 0 and flowerbed[0] == 0 and n == 1
        
        if flowerbed[0] == 0:
            if flowerbed[1] == 0:
                return self.canPlaceFlowers(flowerbed[2:], n-1)
            else:
                return self.canPlaceFlowers(flowerbed[3:], n)
        else:
            return self.canPlaceFlowers(flowerbed[2:], n)