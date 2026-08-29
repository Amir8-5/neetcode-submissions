class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        res = [-1, -1]
        
        tFreq, window = {}, {}

        for c in t:
            if c in tFreq:
                tFreq[c] += 1
            else:
                tFreq[c] = 1
        
        have, need = 0, len(tFreq)
        resLen = float("infinity")
        l = 0
        for r in range(len(s)):
            if s[r] in window:
                window[s[r]] += 1
            else:
                window[s[r]] = 1
            
            if s[r] in tFreq and window[s[r]] == tFreq[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l , r]
                    resLen = (r - l + 1)
                
                window[s[l]] -= 1
                if s[l] in tFreq and window[s[l]] < tFreq[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""


