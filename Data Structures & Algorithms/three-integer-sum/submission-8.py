class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        k = len(nums)-1
        collector = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if nums[i]==nums[i-1] and i>0:
                continue

            j, k = i+1, len(nums)-1
            while j < k:
                sums = nums[i]+nums[j]+nums[k]
                if sums == 0:
                    collector.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j < k:
                        j+=1
                elif sums > 0:
                    k-=1
                else:
                    j+=1
        return collector
