class Solution(object):
    def singleNumber(self, nums):
        number = 0
        for num in nums:
            number ^= num
        return number
        

        
        
        