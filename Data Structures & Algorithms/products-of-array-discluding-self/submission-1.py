class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # find prefix
        prod = 1
        for i in range(len(nums)):
            print("prefix: " + str(prod))
            res[i] = prod
            prod *= nums[i]

        # find suffix
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            print("suffix: " + str(prod))
            res[i] *= prod
            prod *= nums[i]

        return res