# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_mod(start, end, target, nums, first):
            ans = -1
            while start < end:
                m = start + (end-start)//2
                if nums[m] == target:
                    ans = m
                    if first:
                        end = m
                    else:
                        start = m+1
                elif nums[m] < target:
                    start = m+1
                else:
                    end = m
            return ans

        n = len(nums)
        fst = binary_search_mod(0, n, target, nums, True)
        snd = binary_search_mod(0, n, target, nums, False)
        return [fst, snd]