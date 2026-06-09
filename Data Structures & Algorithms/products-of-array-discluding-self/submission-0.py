class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(n^2) for space and time
        """
        output = []
        lastProd = 1
        for i in range(len(nums) - 1):
            lastProd *= nums[i]

            prod = 1
            # before
            for j in range(i):
                prod *= nums[j]

            # after
            for j in range(i + 1, len(nums), 1):
                prod *= nums[j]

            output.append(prod)

        output.append(lastProd)

        return output


