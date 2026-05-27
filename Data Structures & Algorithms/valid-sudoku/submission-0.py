class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [board[i][j] for j in range(9) if board[i][j]!='.']
            column = [board[j][i] for j in range(9) if board[j][i]!='.']

            box_r, box_c = (i//3)*3, (i%3)*3
            box = [board[box_r+r][box_c+c] for r in range(3) for c in range(3) if board[box_r+r][box_c+c] != '.']

            for group in [row, column, box]:
                if len(group) != len(set(group)):
                    return False
        return True