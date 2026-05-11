class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Reverse
        Time: O(n)
        Space: O(n)
        """

        res = []

        n = len(arr)
        next = -1
        for i in range(n - 2, -1, -1):
            next = max(arr[i + 1], next)
            res.append(next)

        res.reverse()
        res.append(-1)
        return res
