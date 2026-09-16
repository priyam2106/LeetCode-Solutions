class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cout=0
        maxi=0
        for i in range(len(nums)):
            if nums[i]==1:
                cout+=1
                maxi=max(maxi,cout)
            elif nums[i]==0:
                cout=0
                
        return maxi