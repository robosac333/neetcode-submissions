class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        store = defaultdict(int)
        for index, num in enumerate(numbers):
            compare = target-num
            if compare in store:
                return [store[compare]+1, index+1]
            store[num] = index