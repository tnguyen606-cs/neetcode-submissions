class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Given:
            sorted numbers in increasing order
            2 <= nums.length <= 3000

        Return:
            target = nums[index1] + nums[index2]
            1-indexed of 2 numbers and index1 < index2
            only 1 value output
        
        Space: O(1)

        Approach: Two pointers
        - l starts at 0: forward
        - r starts at n - 1: backward
        if l + r > target:
            r--
        else if l + r < target:
            l++
        else:
            return l, r

        """

        l = 0
        r = len(numbers) - 1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        
        return []
