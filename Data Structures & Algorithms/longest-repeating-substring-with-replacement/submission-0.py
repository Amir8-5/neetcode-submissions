from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        high = ('', 0)
        l = 0
        res = 0
        for r in range(len(s)):
            freq[s[r]] += 1
            if freq[s[r]] > high[1]:
                high = (s[r], freq[s[r]])
            while (r - l + 1) - high[1] > k:
                freq[s[l]] -= 1
                l += 1 
            res = max(res, r - l + 1)
        return res


            
        

            