class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        melt = []
        r = len(matrix)
        c = len(matrix[0])

        for i in range(r):
            for j in range(c):
                melt.append(matrix[i][j])

        left = 0
        right = len(melt)-1
        mid = (left+right)//2

        while left <= right:
            if melt[mid] == target:
                return True
            
            if melt[mid] > target:
                right = mid-1
                mid = (left+right)//2
            elif melt[mid] < target:
                left = mid+1
                mid = (left+right)//2

        return False
            
