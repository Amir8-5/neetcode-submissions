class Solution:
    def longestPalindrome(self, s: str) -> str:
            resInd = 0
            resLen = 0

            for i in range(len(s)):

                l, r = i, i
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > resLen:
                        resLen = r - l + 1
                        resInd = l
                    r += 1
                    l -= 1
                

                l, r = i, i+1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    if (r - l + 1) > resLen:
                        resLen = r - l + 1
                        resInd = l
                    r += 1
                    l -= 1
                
            return s[resInd:resInd+resLen]