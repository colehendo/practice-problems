from typing import List


class Solution:
    def merge_lists(
        self,
        list_1: List[int],
        list_1_elements: int,
        list_2: List[int],
        _
    ) -> List[int]:
        list_1[list_1_elements: len(list_1)] = list_2
        list_1.sort()
