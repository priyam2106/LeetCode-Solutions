class Solution(object):
    def isPalindrome(self, x):
        if x>=0:
            original=x
            rev=0
            while x>0:
                digit = x%10
                rev=rev*10+digit
                x=x//10
            return rev == original
        else:
            return False
        