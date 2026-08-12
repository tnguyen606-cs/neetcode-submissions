class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given:
            3 <= nums.length <= 3000
            array contains both neg and pos integers
            not sorted array
            not unique array


        Return:
            all triplets [nums[i], nums[j], nums[k]] where sum == 0
            i, j, k are distinct
            no duplicate triplets
            return triplets in any order
        
        Approach: 2 pointers

        for i in len(nums):
            remain = nums[i]

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + remain
                if sum > 0:
                    r--
                elif sum < 0:
                    l++
                else:
                    append to res
                    l++
                    r--


        Time: O(n^2)
        Space: O(1)

        [-4,-1,-1,0,1,2]
        """

        nums.sort() # O(nlogn)

        res = []
        for i in range(len(nums)):
            remain = nums[i]

            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + remain
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    triplet = [remain, nums[l], nums[r]]
                    if triplet not in res:
                        res.append(triplet)
                    l += 1
                    r -= 1
        
        return res





