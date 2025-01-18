class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        s_arr = s.split(" ")
        s_arr.reverse()
        r_str = s_arr[0]
        for a in s_arr[1:]:
            if a == "":
                continue
            r_str = r_str + " " + a
        
        return r_str

sol = Solution()
print(sol.reverseWords("a good   example"))