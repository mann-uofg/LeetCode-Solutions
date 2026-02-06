class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        for num in range(0, k):
            max_element = max(hashmap, key = hashmap.get)
            result.append(max_element)
            hashmap.pop(max_element)
        return result