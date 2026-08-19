class Solution:

    def encode(self, strs: List[str]) -> str:
        e = ''
        for s in strs:
                d = str(len(s)) + '.' + s
                e += d 
        return e

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        strs =[]
        i = 0
        while i < len(s):
            j = i
            while s[j] != '.':
                j += 1 
            n = int(s[i:j])
            strs.append(s[j+1: j+1+n])
            i = j + 1 + n
        return strs


