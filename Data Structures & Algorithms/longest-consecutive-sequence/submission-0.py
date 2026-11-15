class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        answer = 0
        for num in s:
            if num-1 in s:
                continue
            length = 1
            cur = num
            while cur+1 in s:
                cur+=1
                length+=1
            answer = max(answer, length)
        return answer