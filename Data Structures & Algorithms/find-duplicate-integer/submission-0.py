class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """

        Given:
            nums: n+1 integers
            each: [1, n]
            only 1 repeated integer in nums
        Result:
            the repeated integer

        Approach1: Iteration 
            Create a hashset to store unique integer
            If the current integer appears in the set:
                return it
            Time, Space: O(n)
        
        Approach2: 2 Passes
            nums.length == n + 1
            1 <= nums[i] <= n
            Iterate through the array to find the total length
                update the value to multiply -1 at a specific index
                if the value at the specific index < 0:
                    that is visited
            Time: O(n)
            Space: (1)
        """

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                return abs(num)
            nums[idx] *= -1
        return -1

            