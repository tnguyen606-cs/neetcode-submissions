class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Given:
            2 <= heights.length <= 100k
            height is pos+ integer
            heights[i] = height of the ith bar
            duplicate height

        Return:
            maximum amount of water == min(heights[l], heights[r]) * (r - l)

        Approach: 
            - if next > left: left = next
            - if prev > right: right = prev

        Time: O(N)
        Space: O(1)

        """
        # Init 2 pointers
        l = 0
        r = len(heights) - 1

        # set the response to store the max area
        res = 0

        while l < r:
            # compute the current area:
            area = min(heights[l], heights[r]) * (r -l)

            # update the res if the area is larger 
            res = max(res, area)

            # move the pointer at the shorter height
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res
            
