class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given:
            1 <= temp.length <= 100k
            1 <= temp[i] <= 100
            temp[i] = temp on ith day

        Return:
            result array: result[i] = # days after ith day before warmer temp on future
            which means result[i] = idx at next warmer - current idx of temp
            return 0 for result[i] if no next warmer day

        Time: O(n)
        Space: O(n)

        Approach: 
            res
            stack = [] # {temp, idx}
            for temp, idx in temps:
                while stack and tmp > stack[-1][0]:
                    stackT, stackIdx = stack.pop()
                    res[stackIdx] = idx - stackIdx

                stack.append({temp, idx})
        """
        res = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                stackT, stackIdx = stack.pop()
                res[stackIdx] = i - stackIdx

            stack.append([tmp, i])

        return res
        