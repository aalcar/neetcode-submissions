class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                earlier_day = stack.pop()

                ans[earlier_day] = index - earlier_day

            stack.append(index)

        return ans


