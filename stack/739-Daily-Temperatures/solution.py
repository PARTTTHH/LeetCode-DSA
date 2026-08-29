class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        answer = [0] * len(temperatures)
        stack = []

        for i, current_temp in enumerate(temperatures):
            while stack and current_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            stack.append(i)
        return answer