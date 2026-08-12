class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check the string in place using 2 pointers: l, r
        - l starts at index 0: traverse forward
        - r starts at index n - 1: traverse backward

        """

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l].isalnum() and s[r].isalnum() and s[l].lower() != s[r].lower():
                return False

            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue

            l+= 1
            r -=1
                
        return True