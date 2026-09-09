class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        listy = sorted(nums)
        maxxy = 1
        summy = 1
        
        for i in range(1, len(listy)):
            # Skip duplicate values
            if listy[i] == listy[i - 1]:
                continue
            
            # Consecutive number found
            if listy[i] == listy[i - 1] + 1:
                summy += 1
            else:
                # Sequence broken, reset streak
                summy = 1
                
            maxxy = max(maxxy, summy)
            
        return maxxy