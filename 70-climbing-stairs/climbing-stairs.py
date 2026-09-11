class Solution(object):
    def climbStairs(self, n):
        if n ==1 :
            return 1
        elif n ==2:
            return 2
        step1 = 1
        step2 = 2
        for i in range(3,n+1):
             current = step1+ step2
             step1 = step2
             step2 = current
        return step2