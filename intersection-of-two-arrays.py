# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        ans = set()
        n1, n2 = len(nums1), len(nums2)
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                ans.add(nums1[i])
                i += 1
                j += 1
        return ans
