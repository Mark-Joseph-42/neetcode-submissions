class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbaa=sorted(nums)
        checked=set()
        for i in numbaa:
            if i in checked:
                return True
            checked.add(i)
        return False
