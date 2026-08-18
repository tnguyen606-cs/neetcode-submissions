class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
        Given:
            nums1 = m.length
            nums2 = n.length
            sorted nums in -> order
            0 <= m, n <= 1k
            1 <= m + n <= 2k

        Result:
            median value of 2 sorted arrays

        Time: O(m + n)

        Approach:
            - perform merge sorting 
            - return middle element if length % 2 != 0
            - otherwise, return sume() / 2

        """

        m, n = len(nums1), len(nums2)
        l1, l2, r = 0, 0, min(m, n)

        mergeArr = []

        while l1 < m and l2 < n:
            if nums1[l1] <= nums2[l2]:
                mergeArr.append(nums1[l1])
                l1 += 1
            else:
                mergeArr.append(nums2[l2])
                l2 += 1


        while l1 < m:
            mergeArr.append(nums1[l1])
            l1 += 1
        
        while l2 < n:
            mergeArr.append(nums2[l2])
            l2 += 1

        print(mergeArr)

        if len(mergeArr) % 2 != 0:
            mid = len(mergeArr) // 2
            return mergeArr[mid] // 1.0
        
        mid1 = len(mergeArr) // 2
        mid2 = mid1 - 1
        return (mergeArr[mid1] + mergeArr[mid2]) / 2

        

