class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for day, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                previous = stack.pop()
                answer[previous] = day - previous
            stack.append(day)
        return answer