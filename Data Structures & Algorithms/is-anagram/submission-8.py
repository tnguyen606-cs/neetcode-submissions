class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n + m)
        Space: O(1)

        """

        if len(s) != len(t):
            return False

        char1 = [0] * 26
        char2 = [0] * 26
        
        for i in range(len(s)):
            char1[ord(s[i]) - ord('a')] += 1
            char2[ord(t[i]) - ord('a')] += 1
        
        return char1 == char2
