class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new = [i for sublist in matrix for i in sublist]

        left = 0
        right = len(new) - 1
        while left <= right:
            mid = (left + right) // 2
            if new[mid] == target:
                return True
            elif new[mid] > target:
                right = mid - 1
            elif new[mid] < target:
                left = mid + 1
        return False