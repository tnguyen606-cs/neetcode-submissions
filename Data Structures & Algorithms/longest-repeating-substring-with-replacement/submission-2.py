class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """

        Given: 
            s: uppercase english characters
            k: max characters to replace
            1 <= s.length <= 100k
            0 <= k <= s.length
        Return:
            longest substring that contains only one distinct char
        Approach:
            Create a frequency map and init l, maxFreq, res = 0
            Move the right pointer r across the string:
                - Update the frequency of s[r]
                - update the maxFreq with the highest frequency we've seen so far

            If (window size - maxFreq) > k:
                - Reduce the window size from left and the frequency of s[r]
            
            Update the response with the current window size

        Time: O(n)
        Space: O(m)
        """

        count = {}
        l, maxFreq, res = 0, 0, 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res
                        
        