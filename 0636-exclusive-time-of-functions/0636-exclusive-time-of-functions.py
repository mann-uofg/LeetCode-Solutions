class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        timestamp = [item.split(":") for item in logs]
        stack = []
        prev_time = 0

        for item in timestamp:
            func_id = int(item[0])
            action = item[1]
            time = int(item[2])

            if action == "start":
                if stack:
                    result[stack[-1]] += (time - prev_time)
                    pass
                stack.append(func_id)
                prev_time = time
            else:
                result[stack[-1]] += (time - prev_time) + 1
                stack.pop()
                prev_time = time + 1
        return result