class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort = sorted(nums)
        count = 1
        highest_score = 1

        if not nums:
            return 0

        for num in range(len(sort) - 1):
            if ((sort[num]) + 1) == (sort[num + 1]):
                count += 1
            elif (sort[num]) == sort[num + 1]:
                pass
            else:
                count = 1
            if count > highest_score:
                highest_score = count
        return highest_score