from typing import List


class Solution:
    first_array_index = 0
    second_array_index = 0

    current_median = previous_median = 0
    total_len_is_even = None

    @staticmethod
    def get_initial_medians(first_array: List[int], second_array: List[int]) -> int:
        if not first_array:
            return second_array[0]
        if not second_array:
            return first_array[0]

        return min(first_array[0], second_array[0])

    def iterate_index(self, num_list: List[int], index: int):
        if self.total_len_is_even:
            self.previous_median = self.current_median
        self.current_median = num_list[index]

    def find_median(self, first_array: List[int], second_array: List[int], midpoint: int) -> float:
        first_array_len = len(first_array)
        second_array_len = len(second_array)
        total_checked = 0
        self.current_median = self.previous_median = self.get_initial_medians(
            first_array, second_array
        )

        while total_checked <= midpoint:
            if not first_array or self.first_array_index == first_array_len:
                self.iterate_index(second_array, self.second_array_index)
                self.second_array_index += 1

            elif not second_array or self.second_array_index == second_array_len:
                self.iterate_index(first_array, self.first_array_index)
                self.first_array_index += 1

            elif first_array[self.first_array_index] < second_array[self.second_array_index]:
                self.iterate_index(first_array, self.first_array_index)
                self.first_array_index += 1
            else:
                self.iterate_index(second_array, self.second_array_index)
                self.second_array_index += 1

            total_checked += 1

        return (
            float(self.current_median)
            if not self.total_len_is_even
            else (self.current_median + self.previous_median) / 2
        )

    def find_median_sorted_array(self, first_array: List[int], second_array: List[int]) -> float:
        total_len = len(first_array) + len(second_array)
        self.total_len_is_even = total_len % 2 == 0
        midpoint = int(total_len / 2)

        if total_len == 0:
            return float(0)

        return self.find_median(first_array, second_array, midpoint)
