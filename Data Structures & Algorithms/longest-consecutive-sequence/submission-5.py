class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given: 
        - nums.length >= 0
        - not uique numbers
        - neg or pos integers
        - Time: O(n)

        Return: longest consecutive sequences's length

        """

        if len(nums) <= 1:
            return len(nums)
        
        nums.sort()

        res = 0
        count = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            elif nums[i + 1] - nums[i] == 1:
                count += 1
                res = max(res, count)
            else:
                res = max(res, count)
                count = 0

        return res + 1
            