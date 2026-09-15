class Solution(object):
    def plusOne(self, digits):
        num=0
        for d in digits:
            num = num*10+d
        num +=1
        arr = []

        while num > 0:
            arr.append(num % 10)
            num //= 10

        arr.reverse()
        return arr