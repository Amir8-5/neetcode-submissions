class Solution:

    def encode(self, strs: List[str]) -> str:
        
        text = ''
        for st in strs:
            leng = len(st)
            text = text + f"{leng}#{st}"
        return text

    def decode(self, s: str) -> List[str]:
        strs = []
        while s != '':
            delimeter = s.find('#')
            leng = int(s[0:delimeter])
            s = s[delimeter + 1:len(s) + 1]
            strs.append(s[0:leng])
            s = s[leng:len(s)]
        return strs
