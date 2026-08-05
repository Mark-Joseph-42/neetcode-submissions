class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashy=set()
        for i in range(len(nums)):
            if nums[i] in hashy:
                return True
            hashy.add(nums[i])
        return False