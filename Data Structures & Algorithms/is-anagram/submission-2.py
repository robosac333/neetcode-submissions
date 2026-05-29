class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for a, b in zip(s, t):
            d1[a]+=1
            d2[b]+=1
        return d1 == d2
        
        
        