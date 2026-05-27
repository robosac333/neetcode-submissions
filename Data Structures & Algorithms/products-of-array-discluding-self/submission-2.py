class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_cnt = 0
        for num in nums:
            if num!=0:
                product = product*num 
            else:
                zero_cnt+=1
        if zero_cnt > 1:
            return [0]*len(nums)
        return list(map(lambda x: product if x==0 else 0 if zero_cnt ==1 else product // x, nums))