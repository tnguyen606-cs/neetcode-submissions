class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given: palindrome - same forward and backward
        alphanumberic characters (A-Z, a-z) and (0-9)
        1<= s.length <= 1000

        Return: true if valid, false otherwise

        """
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
            
        return newStr == newStr[::-1]