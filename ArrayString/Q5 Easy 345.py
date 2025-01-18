# 345. Reverse Vowels of a String
# Easy

# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

#     1 <= s.length <= 3 * 105
#     s consist of printable ASCII characters.



class Solution(object):
    def reverseVowels(self, s):
        vowel_locations = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        for a in range(len(s)):
            if s[a] in vowels:
                vowel_locations.append(a)
        print(vowel_locations)
        
        for b in range(len(vowel_locations)//2):
            temp = s[vowel_locations[b]]
            s[vowel_locations[b]] = s[vowel_locations[-1-b]]
            s[vowel_locations[-1-b]] = temp
        
        return s
