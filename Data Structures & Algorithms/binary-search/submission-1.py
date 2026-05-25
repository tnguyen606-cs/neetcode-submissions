class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) -1)

    def binarySearch(self, nums: List[int], target: int, low: int, high: int) -> int:

        if low > high:
            return -1

        mid = (high - low) // 2 + low

        if nums[mid] > target:
            return self.binarySearch(nums, target, low, mid - 1)
        elif nums[mid] < target:
            return self.binarySearch(nums, target, mid + 1, high)
        else:
            return mid

