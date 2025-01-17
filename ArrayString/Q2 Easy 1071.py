# 1071. Greatest Common Divisor of Strings
# Easy

# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"

# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"

# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""

 

# Constraints:

#     1 <= str1.length, str2.length <= 1000
#     str1 and str2 consist of English uppercase letters.

def gcd(x,y):
        if y == 0:
            return x
        else:
            return gcd(y,x%y)
class Solution(object):
    
    def gcdOfStrings(self, str1, str2):
        temp = gcd(len(str1), len(str2))
        
        if str2[:temp] * (len(str2)/temp) == str2 and str2[:temp] * (len(str1)/temp) == str1:
            return str2[:temp]
        else:
            return ""
