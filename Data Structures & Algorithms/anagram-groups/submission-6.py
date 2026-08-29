
class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        an = {}

        for word in strs:
            sort = ''.join(sorted(word))
            if sort in an:
                an[sort].append(word)
            else:
                an[sort] = [word]
        return(list(an.values()))
                




        