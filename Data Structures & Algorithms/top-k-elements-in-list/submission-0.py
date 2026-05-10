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
        
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)

        i = 0
        while (len(output) < k):
            output.append(sorted_freq[i][0])
            i += 1

        return output

        
        