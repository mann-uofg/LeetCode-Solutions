class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        product_left = 1
        product_right = 1

        for index in range(len(nums)):
            result[index] = product_left
            product_left *= nums[index]
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= product_right
            product_right *= nums[index]
        return result