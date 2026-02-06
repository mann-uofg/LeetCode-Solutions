class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # result = []
        
        # for i in nums:
        #     count = 0
        #     for j in nums:
        #         if j < i:
        #             count += 1
        #     result.append(count)
        # return result

        # opened hints for optimized

        result = []
        hashmap = {}
        sort = sorted(nums)

        for index, num in enumerate(sort):
            if num not in hashmap:
                hashmap[num] = index
        for num in nums:
            result.append(hashmap[num])
        return result