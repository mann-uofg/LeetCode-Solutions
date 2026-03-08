class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        # Brute-force Solution

        # answer = prices[:]

        # for i in range(len(prices)):
        #     cursor = i + 1
        #     while cursor != len(prices):
        #         if prices[cursor] <= prices[i]:
        #             answer[i] = prices[i] - prices[cursor]
        #             break
        #             cursor += 1
        #         else:
        #             cursor += 1
        # return answer

        # Monotonic Stack Approach

        answer = prices[:]
        stack = []

        for i in range(len(prices)):
            while stack:
                if prices[i] <= prices[stack[-1]]:
                    answer[stack[-1]] = prices[stack[-1]] - prices[i]
                    stack.pop()
                else:
                    break
            stack.append(i)
        return answer