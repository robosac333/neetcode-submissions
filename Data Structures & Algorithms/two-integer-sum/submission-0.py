class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = {}
        for index, num in enumerate(nums):
            compare = target - num
            if compare in check:
                return [check[compare], index]
            check[num] = index