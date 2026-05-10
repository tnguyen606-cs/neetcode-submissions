class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        unique = set()

        for i in range(0, len(nums)):
            if nums[i] in unique:
                return True

            unique.add(nums[i])
        
        return False