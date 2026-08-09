class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numsMap = dict()

        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in numsMap:
                return [numsMap.get(remain), i]
            else:
                numsMap[nums[i]] = i

        return []