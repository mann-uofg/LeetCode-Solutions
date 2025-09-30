class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        tempStr = []
        c1 = 0
        c2 = 0
        len1 = len(word1)
        len2 = len(word2)

        while c1 < len1 and c2 < len2:
            tempStr.append(word1[c1])
            tempStr.append(word2[c2])
            c1 += 1
            c2 += 1

        while c1 < len1:
            tempStr.append(word1[c1])
            c1 += 1

        while c2 < len2:
            tempStr.append(word2[c2])
            c2 += 1

        return ("".join(tempStr))