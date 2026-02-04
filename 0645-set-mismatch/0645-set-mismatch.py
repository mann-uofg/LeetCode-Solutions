class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num in range(1, len(nums) + 1):
            if num in hashmap:
                if hashmap[num] > 1:
                    duplicate = num
            else:
                missing = num
        return [duplicate, missing]