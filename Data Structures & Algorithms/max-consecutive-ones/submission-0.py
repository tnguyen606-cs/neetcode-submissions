class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        """
        time: O(n)
        space: O(1)
        """

        res = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0

            res = max(count, res)

        return res