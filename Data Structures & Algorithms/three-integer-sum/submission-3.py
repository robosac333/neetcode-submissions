class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        collector = []
        if nums[0] > 0:
            return []
        for i , a in enumerate(nums):
            if i > 0 and a==nums[i-1]:
                continue

            l, r = i+1, len(nums)-1
            
            while l < r:
                sums = nums[i] +  nums[l] +  nums[r]
                if sums == 0:
                    collector.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l< r:
                        l+=1
                elif sums > 0:
                    r-=1
                else:
                    l+=1
            
        return collector

            