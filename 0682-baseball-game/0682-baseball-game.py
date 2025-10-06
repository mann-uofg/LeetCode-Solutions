class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for index, char in enumerate(operations):
            try:
                num = int(char)
                score.append(num)
            except:
                if char == "C":
                    score.pop()
                else:
                    if char == "D":
                        score.append(2 * (score[-1]))
                    else:
                        if char == "+":
                            score.append(score[-1] + score[-2])
        return (sum(score))