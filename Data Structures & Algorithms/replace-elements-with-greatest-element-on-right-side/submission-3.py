class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Reverse
        Time: O(n)
        Space: O(n)
        """

        n = len(arr)
        res = [n]
        next = -1
        for i in range(n - 2, -1, -1):
            next = max(arr[i + 1], next)
            res.append(next)

        res.reverse()
        res[n - 1] = -1
        return res
