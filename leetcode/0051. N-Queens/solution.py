from typing import List


class Solution:
    def __init__(self):
        self.n = 0
        self.solutions = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        board = [['.' for j in range(n)] for i in range(n)]
        self.backtrack(board, 0, 0)
        return self.solutions

    def backtrack(self, board, row, queens):
        if queens == self.n:
            self.solutions.append([''.join(row) for row in board])
            return
        if row >= self.n:
            return
        for col in range(self.n):
            if self.valid_placement(board, row, col):
                board[row][col] = 'Q'
                self.backtrack(board, row + 1, queens + 1)
                board[row][col] = '.'

    def valid_placement(self, board, row, col):
        if any(board[i][col] == 'Q' for i in range(row)):
            return False
        # diagonal \
        if any(board[i][j] == 'Q' for i, j in zip(reversed(range(row)), reversed(range(col)))):
            return False
        # diagonal /
        if any(board[i][j] == 'Q' for i, j in zip(reversed(range(row)), range(col + 1, self.n))):
            return False

        return True


if __name__ == '__main__':
    solution = Solution().solveNQueens(10)
    print(solution)
