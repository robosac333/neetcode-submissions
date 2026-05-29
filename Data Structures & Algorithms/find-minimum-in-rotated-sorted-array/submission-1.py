class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1

        if nums[l] <= nums[r]:
            return nums[l]
        else:
            while nums[l]>nums[r]:
                r-=1
        return nums[r+1]