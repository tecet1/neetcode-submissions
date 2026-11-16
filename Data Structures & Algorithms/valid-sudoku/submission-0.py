class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[] for _ in range(9)]
        columns = [[] for _ in range(9)]
        boxes = [[[] for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                number = board[r][c]
                cur_row = rows[r]
                cur_col = columns[c]
                cur_box = boxes[r//3][c//3]

                if number == '.':
                    continue
                if number in cur_row or number in cur_col or number in cur_box:
                    return False
                rows[r].append(number)
                columns[c].append(number)
                boxes[r//3][c//3].append(number)
                
        return True