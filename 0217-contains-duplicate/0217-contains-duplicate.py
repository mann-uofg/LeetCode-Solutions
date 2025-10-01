
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hasDups = set()

        for c in nums:
            if c in hasDups:
                return True
            else:
                hasDups.add(c)
                continue
        return False