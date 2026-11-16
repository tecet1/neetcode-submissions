class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowsize = len(matrix[0])

        left = 0
        right = len(matrix)*len(matrix[0])-1
        mid = (left+right)//2

        while left <= right:
            r = mid//rowsize
            c = mid%rowsize

            if matrix[r][c] == target:
                return True
            
            if matrix[r][c] > target:
                right = mid-1
                mid = (left+right)//2
            elif matrix[r][c] < target:
                left = mid+1
                mid = (left+right)//2

        return False
            
