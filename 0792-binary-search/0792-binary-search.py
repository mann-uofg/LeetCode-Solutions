class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            else:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    if nums[mid] < target:
                        left = mid  + 1
        return -1


        # while left != len(nums):
        #     if nums[left] != target:
        #         left += 1
        #     else:
        #         if nums[left] == target:
        #             return left
        # return -1