class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for char in tokens:
            if char in '+-*/':
                b = stack.pop()
                a = stack.pop()
                if char == '+':
                    stack.append(a + b)
                elif char == '-':
                    stack.append(a - b)
                elif char == '*':
                    stack.append(a * b)
                else:
                    division = a / b
                    if division < 0:
                        stack.append(ceil(division))
                    else:
                        stack.append(int(division))
            else:
                stack.append(int(char))
        return stack[0]