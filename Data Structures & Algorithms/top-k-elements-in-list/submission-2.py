class Solution:
    """
    Time: O(n)
    Space: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        sorted_count = dict(sorted(count.items(), key=lambda item: item[1]))
        print(sorted_count)

        res = [0] * k
        while k > 0:
            curr = sorted_count.popitem()
            res[k - 1] = curr
            k -= 1

        return [x[0] for x in res]




        
        