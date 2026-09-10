class Solution(object):
    def twoSum(self, nums, target):
        hash={}
        # Submit
        for i in range(len(nums)):
            a=nums[i]
            more=target-a
            if more in hash:
                return [hash[more],i]
            hash[nums[i]]=i
        return []