from collections import defaultdict


class Solution:
    def compile_substrings(self, input_str: str, current_max: int) -> int:
        substring_len = 0
        chars_found = defaultdict()

        if current_max >= len(input_str):
            return current_max

        for index, char in enumerate(input_str):
            if char not in chars_found:
                substring_len += 1
                chars_found[char] = index
            else:
                return self.compile_substrings(
                    input_str[chars_found[char] + 1 :], max(current_max, substring_len)
                )

        return max(current_max, substring_len)

    def length_of_longest_substring(self, input_str: str) -> int:
        max_substring = self.compile_substrings(input_str, 0)
        return max_substring
