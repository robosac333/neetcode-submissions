class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, volume = 0, len(height)-1, 0
        while l < r:
            for i in range(l, r):
                volume = max(volume, min(height[i],height[r])*(r-i))
                #print(volume, i, r)

            r-=1
            
        return volume




                             