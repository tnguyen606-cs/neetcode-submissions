class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check the string in place using 2 pointers: l, r
        - l starts at index 0: traverse forward
        - r starts at index n - 1: traverse backward
        Time: O(n)
        Space: O(1)
        """

        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
                
        return True