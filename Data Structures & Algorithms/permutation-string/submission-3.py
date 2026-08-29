from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        for r in range(len(s1), len(s2) + 1):
            sub = s2[l:r]
            print("sub is: " + sub)
            if self.checkPerm(s1, sub):
                return True
            l += 1
        return False
        
    def checkPerm(self, s1, s2):

        if len(s1) != len(s2):
            return False
        
        chars1, chars2 = defaultdict(int), defaultdict(int)
        for i in range(len(s1)):
            chars1[s1[i]] += 1
            chars2[s2[i]] += 1
        return chars1 == chars2

        