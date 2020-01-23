# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t1, t2, t = m-1, n-1, m+n-1
        while t >= 0:
            if t1 >= 0 and t2 >= 0:
                if nums1[t1] > nums2[t2]:
                    nums1[t] = nums1[t1]
                    t1 -= 1
                else:
                    nums1[t] = nums2[t2]
                    t2 -= 1
            elif t1 >= 0 and t2 < 0:
                nums1[t] = nums1[t1]
                t1 -= 1
            elif t2 >= 0 and t1 < 0:
                nums1[t] = nums2[t2]
                t2 -= 1
            t -= 1
