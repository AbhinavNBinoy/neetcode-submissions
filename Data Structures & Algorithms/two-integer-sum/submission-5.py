class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """result=[]
        indices=[]
        count=0
        for i in nums:
            if target==i*2:
                for n in nums:
                    if n==i:
                        count=count+1
                if count>1:
                    for j in range(len(nums)):
                        if nums[j]==i:
                            indices.append(j)
                    return indices
            else:    
                temp=target-i
                if temp in nums:
                    ind1=nums.index(i)
                    ind2=nums.index(temp)
                    result=[ind1,ind2]
                    return result"""
        
        d={}
        result=[]
        for i,num in enumerate(nums):
            sec=target-num
            if sec in d and d[sec] is not None:
                result.append(d[sec])
                result.append(i)
                return result
            else:
                d[num]=i
        
                

        