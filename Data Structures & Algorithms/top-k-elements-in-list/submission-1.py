from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        # 버그 1, 2 수정: 서로 독립된 빈 리스트 n+1개
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counter.items():
            bucket[freq].append(num)          # 대입 대신 추가

        # 버그 3, 4 수정: 빈도가 높은 쪽부터 버킷째로 모으기
        answer = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                answer.append(num)
                if len(answer) == k:
                    return answer
        return answer