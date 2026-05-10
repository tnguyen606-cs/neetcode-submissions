class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        time: O(n)
        space: O(n)
        """

        seen = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            
            seen[nums[i]] = i

        return [0, 0]
    
        
        