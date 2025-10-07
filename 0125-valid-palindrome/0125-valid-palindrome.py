class Solution:
    def isPalindrome(self, s: str) -> bool:
        validString = "".join(c.lower() for c in s if c.isalnum())
        left = 0
        right = len(validString) - 1

        while left < right:
            if validString[left] != validString[right]:
                return False
            else:    
                if validString[left] == validString[right]:
                    left += 1
                    right -= 1
        return True