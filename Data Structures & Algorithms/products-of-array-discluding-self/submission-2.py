class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        """
        [a, b, c, d]
        output[a] = b*c*d = right * left = 1 * left
        output[b] = a*c*d = right * left = a * left
        output[c] = a*b*d = right * left = right * d
        output[d] = a*b*c ...

        no empty output because 2 <= len(nums) <= 100k

        Time: O(n)
        """

        # Create a new array for left multiplication
        left = 1
        leftMult = [1] * len(nums)
        for i in range(len(nums)):
            leftMult[i] = left
            left *= nums[i]

        # Multiply left and the right when traversing from right to left

        res = [1] * len(nums)
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = leftMult[i] * right
            right *= nums[i]

        return res
        