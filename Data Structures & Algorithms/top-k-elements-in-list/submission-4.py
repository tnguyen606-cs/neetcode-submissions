class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        output = []
        seen = dict()

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        arr = []
        for num, cnt in seen.items():
            arr.append([cnt, num])
        arr.sort()

        while len(output) < k:
            output.append(arr.pop()[1])

        return output