class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * 2 * n
        for i in range(n * 2):
            if (i >= n):
                res[i] = nums[i - n]
            else:
                res[i] = nums[i]
        return res
        