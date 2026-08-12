class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Given:
            non-neg integers
            1 <= heights.length
            duplicate heights
            non-sorted heights

        Return:
            max area = max wall on that side - height at that position

        Approach:
            l = 0
            r = len(heights) - 1
            leftMax = heights[l]
            rightMax = heigths[r]
            res = 0
            while l < r:
                
                if leftMax < rightMax:
                    l += 1
                    leftMax = max(leftMax, heights[l])
                    res += leftMax
                else:
                    r -= 1
                    rightMax = max(rightMax, heights[r])
                    res += rightMax
            return res


        Time: O(n)
        Space: O(1)

        """
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        while l < r:
            
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        