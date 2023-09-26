from typing import List


class Solution:
    def merge_lists(
        self,
        list_1: List[int],
        list_1_position: int,
        list_1_elements: int,
        list_2: List[int],
        list_2_position: int,
        list_2_elements: int,
        merged_list: List[int]
    ) -> List[int]:
        if list_1_position >= list_1_elements and list_2_position >= list_2_elements:
            return merged_list

        if list_1_position >= list_1_elements:
            merged_list.extend(list_2[list_2_position:list_2_elements + 1])
            return merged_list

        elif list_2_position >= n:
            merged_list.extend(list_1[list_1_position:list_1_elements + 1])
            return merged_list

        curr_list_1 = list_1[list_1_position]
        curr_list_2 = list_2[list_2_position]

        if curr_list_1 <= curr_list_2:
            merged_list.append(curr_list_1)
            list_1_position += 1
        else:
            merged_list.append(curr_list_2)
            list_2_position += 1

        return self.merge_lists(
            list_1,
            list_1_position,
            list_1_elements,
            list_2,
            list_2_position,
            list_2_elements,
            merged_list
        )

    def merge_handler(
        self,
        list_1: List[int],
        list_1_elements: int,
        list_2: List[int],
        list_2_elements: int
    ) -> List[int]:
        list_1_position = 0
        list_2_position = 0
        merged_list = []

        self.merge_lists(
            list_1,
            list_1_position,
            list_1_elements,
            list_2,
            list_2_position,
            list_2_elements,
            merged_list
        )

        return merged_list
