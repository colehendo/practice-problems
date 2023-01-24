from typing import Union


class MedianFinder:
    def __init__(self):
        self.int_list = []
        self.int_list_len = 0

    def add_num_to_non_empty_list(self, num: int):
        self.int_list_len += 1
        if num >= self.int_list[-1]:
            self.int_list.append(num)
            return

        for index, value in enumerate(self.int_list):
            if num <= value:
                self.int_list.insert(index, num)
                break

    def add_num(self, num: int):
        self.int_list_len = 1
        self.int_list.append(num)
        self.addNum = self.add_num_to_non_empty_list

    def get_median_of_even_len_list(self) -> float:
        midpoint = int(self.int_list_len / 2)
        lower_median_index = midpoint - 1

        lower_median = self.int_list[lower_median_index]
        upper_median = self.int_list[midpoint]

        return (lower_median + upper_median) / 2

    def get_median_of_odd_len_list(self) -> Union[int, float]:
        median_index = int(self.int_list_len / 2)
        return self.int_list[median_index]

    def find_median(self) -> Union[int, float]:
        if self.int_list_len == 0:
            return

        if self.int_list_len % 2 == 0:
            return self.get_median_of_even_len_list()
        else:
            return self.get_median_of_odd_len_list()
