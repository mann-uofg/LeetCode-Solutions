class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        cursor = 0

        while cursor != len(nums):
            if nums[cursor] in hashmap:
                hashmap[nums[cursor]] += 1
            else:
                hashmap[nums[cursor]] = 1
            cursor += 1
            max_num = max(hashmap, key = hashmap.get)
        return max_num