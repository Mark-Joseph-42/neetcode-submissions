class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check={}
        for i in nums:
            if i not in check:
                check[i]=1
            else:
                check[i]+=1
        checkers=list(check.items())
        checkers.sort(key=lambda x: x[1], reverse=True)
        output=[]
        for i in range(k):
            output.append(checkers[i][0])
        return output