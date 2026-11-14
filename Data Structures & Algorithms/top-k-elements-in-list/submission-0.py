from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict(Counter(nums))
        l = [(v,i) for i,v in counter.items()]
        l = sorted(l, key=lambda x:x[0], reverse=True)
        result = [i for v,i in l[:k]]
        return result