class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy={}
        for i in range(len(nums)):
            z=nums[i]
            if(target-z in mappy):
                return[mappy[target-z],i]
            mappy[z]=i