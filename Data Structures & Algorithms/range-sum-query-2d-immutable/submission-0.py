class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix)+1
        c = len(matrix[0])+1
        p = [[0] * c for _ in range(r)]

        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                p[i+1][j+1]=p[i][j+1]+p[i+1][j]+matrix[i][j]-p[i][j] # 

        self.p = p


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        p = self.p
        return p[row2+1][col2+1]-p[row1][col2+1]-p[row2+1][col1]+p[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)