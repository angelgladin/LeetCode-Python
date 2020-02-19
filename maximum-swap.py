# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        l = [int(x) for x in str(num)]
        max_so_far = (-1, -1,)
        candidate = (-1, -1,)
        
        for i in range(len(l)-1, -1, -1):
            if l[i] > max_so_far[0]:
                max_so_far = (l[i], i,)
            elif l[i] < max_so_far[0]:
                candidate = (max_so_far[1], i,)
        
        if candidate[0] == -1:
            return num
        
        aux = l[candidate[0]]
        l[candidate[0]] = l[candidate[1]]
        l[candidate[1]] = aux
        
        return int(''.join(map(str, l)))
