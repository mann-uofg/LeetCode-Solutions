class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]

        for i in range(len(prices)):
            cursor = i + 1
            while cursor != len(prices):
                if prices[cursor] <= prices[i]:
                    answer[i] = prices[i] - prices[cursor]
                    break
                    cursor += 1
                else:
                    cursor += 1
        return answer