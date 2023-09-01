from typing import List


class Solution:
    @staticmethod
    def compile_rows_of_substrings(
        initial_string: str, num_rows: int, rows_of_strings: List[str]
    ):
        current_row = 0
        reverse = False

        for letter in initial_string:
            rows_of_strings[current_row] += letter

            if reverse:
                if current_row == 0:
                    reverse = False
                    current_row += 1
                else:
                    current_row -= 1
            else:
                if current_row == num_rows - 1:
                    reverse = True
                    current_row -= 1
                else:
                    current_row += 1

    def convert(self, initial_string: str, num_rows: int) -> str:
        if num_rows == 1 or len(initial_string) <= num_rows:
            return initial_string

        rows_of_strings = ["" for _ in range(num_rows)]
        self.compile_rows_of_substrings(initial_string, num_rows, rows_of_strings)

        zigzag_string = "".join(rows_of_strings)
        return zigzag_string
