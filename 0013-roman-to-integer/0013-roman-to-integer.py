class Solution:
    def romanToInt(self, s: str) -> int:
        hashTable = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        i = 0
        summ = 0

        while i < len(s):
            if (i + 1) < len(s) and hashTable[s[i]] < hashTable[s[i + 1]]:
                summ += hashTable[s[i + 1]] - hashTable[s[i]]
                i += 2
            else:
                if i == len(s):
                    summ += hashTable[s[i]]
                else:
                    summ += hashTable[s[i]]
                    i += 1
        return summ