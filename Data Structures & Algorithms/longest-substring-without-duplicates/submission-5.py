class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        l, r, maxf = 0, 0, 0
        while r < len(s):
            while count[s[r]]>0:
                count[s[l]]-=1
                l+=1
            count[s[r]]+=1
            maxf = max(maxf, r-l+1)
            r+=1
        return maxf
        