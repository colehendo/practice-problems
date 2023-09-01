from typing import List


class Solution:
    board = [[]]

    def check_validity(self, num: int, row_to_check: int, col_to_check: int) -> bool:
        if any(
            value == num and col != col_to_check
            for col, value in enumerate(self.board[row_to_check])
        ):
            return False

        if any(
            row[col_to_check] == num and row_index != row_to_check
            for row_index, row in enumerate(self.board)
        ):
            return False

        row_block = int(row_to_check / 3)
        column_block = int(col_to_check / 3)

        for row in range(row_block * 3, (row_block * 3) + 3):
            for col in range(column_block * 3, (column_block * 3) + 3):
                if row == row_to_check and col == col_to_check:
                    continue
                if self.board[row][col] == num:
                    return False

        return True

    def build_board(self) -> bool:
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != ".":
                    continue

                for num in "123456789":
                    num_valid = self.check_validity(num, row, col)
                    if num_valid:
                        self.board[row][col] = num
                        board_valid = self.build_board()
                        if not board_valid:
                            self.board[row][col] = "."
                        else:
                            return True

                return False
        return True

    def solve_sudoku(self, board: List[List[str]]):
        self.board = board
        self.build_board()
