class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        posNums = min(abs(num) for num in nums)
        if posNums in nums:
            return posNums
        else:
            return -posNums
        
        