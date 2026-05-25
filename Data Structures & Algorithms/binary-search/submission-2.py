class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums)

        while l < h:
            mid = l + ((h - l) // 2)

            if nums[mid] >= target:
                h = mid
            else:
                l = mid + 1
        return l if (l < len(nums) and nums[l] == target) else -1