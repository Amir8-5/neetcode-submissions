class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        chars = list(s)
        longestSub = []
        for char in chars:
            if char in longestSub:
                break
            longestSub.append(char)
        
        return max(len(longestSub), self.lengthOfLongestSubstring(s[1:]))