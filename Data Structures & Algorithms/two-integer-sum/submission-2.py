class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mappy={}
        for i in range(len(nums)):
            num=nums[i]
            req=target-num
            if req in mappy:
                return [mappy[req], i]
            mappy[num]=i
