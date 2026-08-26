class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """

        Given:
            0 <= s.length <= 50k
            s: ASCII chars
        
        Return:
            longest substring without duplicate characters

        Approach:
            Create a set to store the unique chars
            Create a length to store the max substring length
            Create L, R to store first, last substring indices
            Iterate through the s:
                while c in set:
                    remove the previous chars until the next unique char
                    by calling remove method and update L to the next
                update R to the next
                find max_length between current max_length and R - L
            
        Time: O(n)
        Space: O(1)
        """
        
        max_length = 0
        char_set = set()
        L = 0

        for R, C in enumerate(s):
            while C in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(C)
            R += 1
            max_length = max(max_length, R - L)
        
        return max_length