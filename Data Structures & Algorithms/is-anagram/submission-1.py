class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        if len(s) != len(t):
            return False
        for a, b in zip(s, t):
            d1[a]+=1
            d2[b]+=1
        for a, b in zip(s, t):
            if not d1[b] and not d2[a]:
                return False
            else:
                d1[b]-=1
                d2[a]-=1
        print(d1.values(), d2.values())
        for v1, v2 in zip(d1.values(), d2.values()):
            if v1 or v2:
                return False
        return True
        
        