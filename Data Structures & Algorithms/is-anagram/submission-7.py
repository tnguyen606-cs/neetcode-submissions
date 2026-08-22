class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n + m)
        Space: O(1)

        """

        return sorted(s) == sorted(t)