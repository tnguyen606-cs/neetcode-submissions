class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Time: O(n + m)
        Space: O(1)

        """

        if len(s) != len(t):
            return False

        char = [0] * 26
        
        for i in range(len(s)):
            char[ord(s[i]) - ord('a')] += 1
            char[ord(t[i]) - ord('a')] -= 1
        
        for c in char:
            if c != 0:
                return False
        return True
