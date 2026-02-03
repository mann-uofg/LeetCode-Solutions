class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cursor = 0
        counter = 0
        high_score = 0

        while cursor != len(nums):
            if nums[cursor] == 1:
                cursor += 1
                counter += 1
            else:
                counter = 0
                cursor += 1
            if counter > high_score:
                high_score = counter
        return high_score