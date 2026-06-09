class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        O(nlogn)
        """

        if len(nums) < 2:
            return len(nums)

        nums.sort()

        longest = 0
        curLength = 1
        for i in range(1, len(nums), 1):
            if nums[i] - nums[i - 1] == 1:
                curLength += 1
            elif nums[i] - nums[i - 1] > 1:
                curLength = 1

            longest = max(longest, curLength)

        return longest
        