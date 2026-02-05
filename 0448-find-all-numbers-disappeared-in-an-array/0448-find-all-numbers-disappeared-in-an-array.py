class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        hashmap = {}
        result = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num in range(1, len(nums) + 1):
            if num not in hashmap:
                result.append(num)
        return result