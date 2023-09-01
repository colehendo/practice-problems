from typing import Tuple


class Solution:
    @staticmethod
    def get_sign_and_starting_index(first_char: str) -> Tuple[bool, int]:
        if first_char == "-":
            return True, 1
        else:
            if first_char == "+":
                return False, 1
            else:
                return False, 0

    @staticmethod
    def get_int_value(extracted_num: str) -> int:
        extracted_num_as_int = int(extracted_num)

        if extracted_num_as_int < -(2**31):
            return -(2**31)
        if extracted_num_as_int > (2**31 - 1):
            return 2**31 - 1

        return extracted_num_as_int

    def atoi(self, input_str: str) -> int:
        stripped_input_str = input_str.lstrip()
        if not stripped_input_str:
            return 0

        extracted_num = ""
        first_char = stripped_input_str[0]
        is_negative, starting_index = self.get_sign_and_starting_index(first_char)

        for char in stripped_input_str[starting_index:]:
            if not char.isdigit():
                break
            extracted_num += char

        extracted_num = extracted_num.lstrip("0")
        if not extracted_num:
            return 0
        if is_negative:
            extracted_num = f"-{extracted_num}"

        return self.get_int_value(extracted_num)
