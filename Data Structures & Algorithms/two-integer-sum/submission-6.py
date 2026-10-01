class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        result=[]
        for i,num in enumerate(nums):
            sec=target-num
            if sec in d:
                result.append(d[sec])
                result.append(i)
                return result
            else:
                d[num]=i