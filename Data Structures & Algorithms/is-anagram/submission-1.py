class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        d=dict()
        freq=dict()
        for i in s:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        for i in t:
            if i in freq:
                freq[i]=freq[i]+1
            else:
                freq[i]=1
        if d==freq:
            return True
        else:
            return False