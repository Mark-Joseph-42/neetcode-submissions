class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        summy=0
        while(left<right):
            summy=nums[left]+nums[right]
            if(summy>target):
                right-=1
            elif(summy==target):
                return[left+1,right+1]
            else:
                left+=1