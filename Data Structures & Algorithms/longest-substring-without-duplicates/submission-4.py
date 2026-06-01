class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i = 0
        # max_len = 0
        # for i in range(len(s)):
        #     seen = set()
        #     for j in range(i, len(s)):
        #         if s[j] in seen:
        #             break
        #         seen.add(s[j])
        #         max_len = max(max_len, len(seen))
        # return max_len

        seen = set()
        l, maxlen= 0, 0
        if len(s) == 1:
            return 1
        if not s:
            return 0
        
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[r])
            maxlen = max(maxlen, r-l+1)
        return maxlen
            
