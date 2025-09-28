class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {"(" : ")", "{" : "}", "[" : "]"}
        charStack = []

        for c in s:
            if c in charMap:
                charStack.append(c)
            else:
                if not charStack or charMap[charStack.pop()] != c:
                    return False
        return not charStack



