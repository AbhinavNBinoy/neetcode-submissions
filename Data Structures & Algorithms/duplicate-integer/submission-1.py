class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=[]
        for i in nums:
            if i not in hashset:
                hashset.append(i)
        if len(hashset)==len(nums):
            return False
        else:
            return True

        