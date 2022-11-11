from collections import defaultdict


class Solution:
    def compile_substrings(self, s: str, current_max: int) -> int:
        substring = ""
        chars_found = defaultdict(lambda: None)

        for index, char in enumerate(s):
            if chars_found[char] is None:
                substring += char
                chars_found[char] = index
            else:
                return self.compile_substrings(
                    s[chars_found[char] + 1 :], max(current_max, len(substring))
                )

        return max(current_max, len(substring))

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_substring = self.compile_substrings(s, 0)
        return max_substring
