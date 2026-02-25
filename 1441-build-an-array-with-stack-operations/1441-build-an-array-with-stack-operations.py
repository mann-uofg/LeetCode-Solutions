class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_index = 0

        for num in range(1, target[-1] + 1):
            if num == target[target_index]:
                result.append("Push")
                target_index += 1
                n -= 1
            else:
                result.append("Push")
                result.append("Pop")
                n -= 1
            if n == 0:
                break
        return result