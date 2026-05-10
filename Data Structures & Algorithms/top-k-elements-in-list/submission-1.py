class Solution:
    """
    Clarification:
    1. Is the array sorted?
    2. Are duplicated numbers arranged together?
    3. Are we sure that there is always an output?
    
    Understanding:
    [1,2,2,3,3,3]

    map:
    1 -> 1
    2 -> 2
    3 -> 3

    k = 2 -> output = [2, 3]

    Time: O(nlogn)
    Space: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = []
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        sorted_arr = []
        for num, count in freq.items():
            sorted_arr.append([count, num])
        sorted_arr.sort()

        while len(output) < k:
            output.append(sorted_arr.pop()[1])

        return output

        
        