class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        left = 0
        right = (len(nums) // 2)

        while (left != (len(nums) // 2) and right != len(nums)):
            result.append(nums[left])
            result.append(nums[right])
            left += 1
            right += 1
        return result 