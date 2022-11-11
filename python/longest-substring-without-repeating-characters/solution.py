from collections import defaultdict
from typing import List


class Solution:
    def compile_substrings(self, s: str, all_substrings: List[int]) -> List[int]:
        substring = ""
        chars_found = defaultdict(lambda: None)

        for index, char in enumerate(s):
            if chars_found[char] is None:
                substring += char
                chars_found[char] = index
            else:
                all_substrings.append(len(substring))
                return self.compile_substrings(
                    s[chars_found[char] + 1 :], all_substrings
                )

        all_substrings.append(len(substring))
        return all_substrings

    def lengthOfLongestSubstring(self, s: str) -> int:
        all_substrings = self.compile_substrings(s, [])
        return max(all_substrings)
