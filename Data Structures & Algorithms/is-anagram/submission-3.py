class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_let = {}
        t_let = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in s_let:
                s_let[s[i]] += 1
            else:
                s_let[s[i]] = 1
            
            if t[i] in t_let:
                t_let[t[i]] += 1
            else:
                t_let[t[i]] = 1
        return s_let == t_let
            


        