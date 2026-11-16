import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        answer = -1
        
        start = 1
        end = 10**9+1

        while start <= end:
            k = (start+end)//2
            time = 0
            for pile in piles:
                time += math.ceil(pile/k)
            if time <= h:
                answer = k
                end = k-1
            elif time > h:
                start = k+1

        return answer