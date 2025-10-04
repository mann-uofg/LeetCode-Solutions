class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums2 = []

        for num in nums:
            squared = num * num
            nums2.append(squared)
            continue
        nums2.sort()
        return nums2
        