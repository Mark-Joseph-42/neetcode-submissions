class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=set()
        n=len(nums)
        for i in range (n):
            if(nums[i] in a):
                return True
            a.add(nums[i])
        return False