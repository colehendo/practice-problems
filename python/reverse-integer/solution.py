class Solution:
    def reverse_integer(self, initial_int: int) -> int:
        if initial_int == 0:
            return 0
        int_as_string = str(initial_int)

        if int_as_string.startswith("-"):
            negative_number = True
            int_as_string = int_as_string[1:]
        else:
            negative_number = False

        reversed_int = str(int_as_string)[::-1]
        stripped_int = reversed_int.lstrip("0")

        if negative_number:
            stripped_int = f"-{stripped_int}"

        final_int = int(stripped_int)
        return final_int if -(2**31) < final_int < (2**31 - 1) else 0
