class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num in hashmap:
            if hashmap[num] == 1:
                return num