class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Given:
            piles[i] == # bananas
            h = # hours to eat all bananas
            1 <= piles.length <= h
            1 <= piles[i]

        Result:
            k = min # hours to eat all bananas
            k <= h

        Approach:
            start = smallest pile
            end = largest pile
            k = largest pile
            while start < end:
                mid = (start + end) // 2
                
                avgH = calculate the hours taken from the mid
                if avgH > h:
                    start = mid + 1
                else:
                    end = mid - 1
            
        """ 


        l, r = 1, max(piles)

        while l <= r:
            m = (l + r) // 2
            
            totalHours = 0
            for pile in piles:
                totalHours += math.ceil(pile / m)

            if totalHours > h:
                l = m + 1
            else:
                r = m - 1
        return l





