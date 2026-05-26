class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicti = defaultdict(int)
        for num in nums:
            dicti[num] +=1
        compare = sorted(dicti.values())[::-1][:k]
        return [key for key, value in dicti.items() if value in compare][:k]