class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sette=set()
        n=len(nums)
        for i in range(n):
            if nums[i] in sette:
                return True
            else:
                sette.add(nums[i])
        return False