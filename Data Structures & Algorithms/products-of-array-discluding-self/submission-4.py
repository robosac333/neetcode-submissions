class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # zero_cnt = 0
        # for num in nums:
        #     if num!=0:
        #         product = product*num 
        #     else:
        #         zero_cnt+=1
        # if zero_cnt > 1:
        #     return [0]*len(nums)
        # return list(map(lambda x: product if x==0 else 0 if zero_cnt ==1 else product // x, nums))
        res = [1]*len(nums)
        res2 = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        nums.reverse()
        for i in range(len(nums)):
            res2[i] = postfix
            postfix *= nums[i]
        res2 = reversed(res2)
        return list(map(lambda x, y: x *y, res, res2))
