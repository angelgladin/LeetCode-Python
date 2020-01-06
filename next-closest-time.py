# https://leetcode.com/problems/next-closest-time/

class Solution:
    def nextClosestTime(self, time: str) -> str:
        valid_nums = { x for x in time if x != ':' }
        hour = int(time[0:2])
        minute = int(time[3:5])
        while True:
            if minute + 1 == 60:
                hour += 1
                minute = 0
            else:
                minute += 1
            
            if hour == 24:
                hour = 0
            
            h = str(hour) if hour > 9 else '0' + str(hour)
            m = str(minute) if minute > 9 else '0' + str(minute)
            valid = True
            for x in h:
                valid &= x in valid_nums
            for x in m:
                valid &= x in valid_nums
            if valid:
                return '{}:{}'.format(h, m)
        return ''
