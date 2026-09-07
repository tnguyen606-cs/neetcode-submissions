class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Time: O(n)
        Space: (N)
        """

        left = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            left[i] = prev
            prev *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            curr = nums[i]
            nums[i] = post * left[i]
            post *= curr

        return nums