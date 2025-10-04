class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqS = {}
        freqT = {}

        if len(s) != len(t):
            return False

        for c in s:
            freqS[c] = freqS.get(c, 0) + 1
        
        for c in t:
            freqT[c] = freqT.get(c, 0) + 1
        
        return freqS == freqT
