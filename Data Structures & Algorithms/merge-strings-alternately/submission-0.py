class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0, 0
        len1, len2 = len(word1), len(word2)
        res = []

        while l1 < len1 and l2 < len2:
            res.append(word1[l1])
            res.append(word2[l2])
            l1 += 1
            l2 += 1
        
        if l1 == len1 and l2 < len2:
            res.append(word2[l2:])
        elif l2 == len2 and l1 < len1:
            res.append(word1[l1:])
        
        return "".join(res)
