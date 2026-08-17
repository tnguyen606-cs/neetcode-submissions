class Solution:
    def findMin(self, nums: List[int]) -> int:

        """

        Institution:
            Array Rotation: 

        Given:
            sorted in ascending order
            rotated between 1 and n times
            rotates
            1 <= nums.length

        Result:
            the smallest element of the array

        Approach: Binary search 
            The smallest is where the cliff occurrs


        Time: O(logn)
        Space: O(1)

        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m - 1] > nums[m] and nums[m] < nums[m + 1]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return nums[l]