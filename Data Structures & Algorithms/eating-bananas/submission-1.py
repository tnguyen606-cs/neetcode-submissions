class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        """
        piles = [1,4,3,2], h = 9
        rate=1: [1,4,3,2] = 10 
        rate=2: [1,2,2,1] = 6
        rate=3: [1,2,1,1] = 5
        rate=4: [1,1,1,1] = 4

        rate range: [1, max(piles)]
        BS until total hours > h

        more h == less rate
        less h == more rate
        """
        maxRate = max(piles) # O(n)
        rate, l, r = maxRate, 1, maxRate

        while l <= r:
            mid = (l + r) // 2

            totalHours = 0
            for pile in piles:
                print(f"mid={mid}. eat={math.ceil(pile / mid)}")
                totalHours += math.ceil(pile / mid)
            print(f"total={totalHours}")

            if totalHours > h:
                l = mid + 1
            elif totalHours <= h:
                r = mid - 1
                rate = min(mid, rate)

        return rate
                
