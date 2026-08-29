class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        if not s:
            return 0
        high = 1
        chars = set()
        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
                high = max(high, r - l + 1)
            else:
                while l < r and s[r] in chars:
             
                    chars.remove(s[l])
                    l += 1
                chars.add(s[r])
        return high

        