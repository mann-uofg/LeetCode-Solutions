class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i = 0
        answer = []

        while i < len(nums):
            start = nums[i]

            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i += 1

            if start != nums[i]:
                answer.append(str(start) + '->' + str(nums[i]))
            else:
                answer.append(str(nums[i]))

            i += 1
        return answer
