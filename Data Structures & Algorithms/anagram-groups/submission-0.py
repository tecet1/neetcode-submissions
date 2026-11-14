from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for s in strs:
            key = ''.join(sorted(s))
            dic.setdefault(key, []).append(s)
        
        return [d for d in dic.values()]

        