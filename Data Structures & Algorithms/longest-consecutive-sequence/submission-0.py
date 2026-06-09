class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(n^2) for time
        O(n) for space
        """

        numSet = set(nums)
        longest = 0

        for num in nums:
            if num in numSet:
                length = 1

                while (num + length) in numSet:
                    length += 1

                longest = max(longest, length)

        return longest
