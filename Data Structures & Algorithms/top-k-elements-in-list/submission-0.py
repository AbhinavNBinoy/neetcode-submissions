class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for num in nums:
            if num in d:
                d[num]=d[num]+1
            else:
                d[num]=1
        result=[]
        for i in range(k):
            m=max(d,key=d.get)
            result.append(m)
            del d[m]
        return result