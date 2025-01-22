# 1456. Maximum Number of Vowels in a Substring of Given Length
# Medium

# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:

# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

 

# Constraints:

#     1 <= s.length <= 105
#     s consists of lowercase English letters.
#     1 <= k <= s.length



class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        count = 0
        max_sub = 0
        first_sub = s[0:k]
        for c in first_sub:
            if c in vowels:
                count += 1
                max_sub += 1

        for i in range(k,len(s)):
            if s[i] in vowels:
                count += 1
            if s[i - k] in vowels:
                count -= 1
            max_sub = max(max_sub, count)
        return max_sub