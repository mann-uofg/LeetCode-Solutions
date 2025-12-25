# class Solution:
#     def findClosestNumber(self, nums: List[int]) -> int:
#         posNums = min(abs(num) for num in nums)
#         if posNums in nums:
#             return posNums
#         else:
#             return -posNums
        
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        arr2 = []
        for num in nums:
            arr2.append(abs(num))
            arr2.sort()
        if arr2[0] in nums:
            return arr2[0]
        else:
            return -arr2[0]

        