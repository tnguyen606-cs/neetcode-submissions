class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        """
        time: O(n)
        space: O(1)
        """
        res = cnt = 0
        for num in nums:
            cnt += 1 if num else -cnt
            res = max(res, cnt)
        return res