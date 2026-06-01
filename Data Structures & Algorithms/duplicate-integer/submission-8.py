class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numba=sorted(nums)
        checked=set()
        for i in numba:
            if i in checked:
                return True
            checked.add(i)
        return False
