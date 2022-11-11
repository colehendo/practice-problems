from collections import defaultdict


class Solution:
    def compile_substrings(self, s: str, current_max: int) -> int:
        substring_len = 0
        chars_found = defaultdict(lambda: None)

        for index, char in enumerate(s):
            if chars_found[char] is None:
                substring_len += 1
                chars_found[char] = index
            else:
                return self.compile_substrings(
                    s[chars_found[char] + 1 :], max(current_max, substring_len)
                )

        return max(current_max, substring_len)

    def length_of_longest_substring(self, s: str) -> int:
        max_substring = self.compile_substrings(s, 0)
        return max_substring
