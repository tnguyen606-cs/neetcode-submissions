class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        Given: distinct integers, sorted in ascending order
            1<= nums.length <= 10000

        Need: Search for target in nums
            If found, return its index
            Else: return -1

        Time: O(logn)
        Space: O(1)

        Approach: Binary Search

        """

        left = 0
        right = len(nums)

        while left < right:
            mid = (right - left) // 2 + left

            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        
        return -1

        