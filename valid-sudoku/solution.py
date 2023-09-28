from typing import List


class Solution:
    def check_rows(self, board: List[List[str]]) -> bool:
        for row in board:
            filtered_row = [value for value in row if value != "."]
            if len(filtered_row) > len(set(filtered_row)):
                return False

        return True

    def check_columns(self, board: List[List[str]]) -> bool:
        for column_index in range(0, 9):
            filtered_column = [row[column_index] for row in board if row[column_index] != "."]
            if len(filtered_column) > len(set(filtered_column)):
                return False

        return True


    def check_containers(self, board: List[List[str]]) -> bool:
        for row_counter in range(0, 9, 3):
            for column_counter in range(0, 9, 3):
                container = []
                for row in range(0, 3):
                    for column in range(0, 3):
                        value = board[row + row_counter][column + column_counter]
                        if value != ".":
                            container.append(value)

                if len(container) > len(set(container)):
                    return False

        return True


    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # This checks each function one at a time,
        # resulting in more code than an all() statement,
        # but ensures if one check fails the following ones
        # do not have to run
        rows_are_valid = self.check_rows(board)
        if not rows_are_valid:
            return False

        columns_are_valid = self.check_columns(board)
        if not columns_are_valid:
            return False

        containers_are_valid = self.check_containers(board)
        if not containers_are_valid:
            return False

        return True
