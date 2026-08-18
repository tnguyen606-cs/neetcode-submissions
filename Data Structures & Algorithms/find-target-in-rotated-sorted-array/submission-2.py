class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """

        Given:
            sorted unique nums
            rotated between 1 and n times
            1 <= nums.length

        Result:
            index of target; else: -1

        Time: O(logn)
        Space: O(1)

        """

        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        pivot = l

        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        result = binary_search(0, pivot -1)

        if result != -1:
            return result

        return binary_search(pivot, len(nums) -1)






