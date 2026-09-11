class Solution(object):
    def nextPermutation(self, nums):
        n=len(nums)
        ind=-1
        def reverse(nums,start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                ind=i
                break
        if ind==-1:
            rev=reverse(nums,0,n-1)
            return nums
        for i in range(n-1,ind,-1):
            if nums[i]>nums[ind]:
                nums[i],nums[ind]=nums[ind],nums[i]
                break
        reverse(nums,ind+1,n-1)
        return nums
        