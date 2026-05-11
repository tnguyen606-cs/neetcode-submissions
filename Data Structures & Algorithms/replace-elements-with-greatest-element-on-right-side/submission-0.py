class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Bruteforce
        Time: O(n^2)
        Space: O(n)
        """

        res = []

        n = len(arr)
        for i in range(n - 1):
            curr = max(arr[(i + 1):n])
            res.append(curr)

        res.append(-1)
        return res
