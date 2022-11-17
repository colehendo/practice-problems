from typing import List


class Solution:
    nums1_index = 0
    nums2_index = 0

    current_median = previous_median = 0
    total_len_is_even = None

    @staticmethod
    def get_initial_medians(nums1: List[int], nums2: List[int]) -> int:
        if not nums1:
            return nums2[0]
        if not nums2:
            return nums1[0]

        return min(nums1[0], nums2[0])

    def iterate_index(self, num_list: List[int], index: int):
        if self.total_len_is_even:
            self.previous_median = self.current_median
        self.current_median = num_list[index]

    def find_median(self, nums1: List[int], nums2: List[int], midpoint: int) -> float:
        nums1_len = len(nums1)
        nums2_len = len(nums2)
        total_checked = 0
        self.current_median = self.previous_median = self.get_initial_medians(
            nums1, nums2
        )

        while total_checked <= midpoint:
            if not nums1 or self.nums1_index == nums1_len:
                self.iterate_index(nums2, self.nums2_index)
                self.nums2_index += 1

            elif not nums2 or self.nums2_index == nums2_len:
                self.iterate_index(nums1, self.nums1_index)
                self.nums1_index += 1

            elif nums1[self.nums1_index] < nums2[self.nums2_index]:
                self.iterate_index(nums1, self.nums1_index)
                self.nums1_index += 1
            else:
                self.iterate_index(nums2, self.nums2_index)
                self.nums2_index += 1

            total_checked += 1

        return (
            float(self.current_median)
            if not self.total_len_is_even
            else (self.current_median + self.previous_median) / 2
        )

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2)
        self.total_len_is_even = total_len % 2 == 0
        midpoint = int(total_len / 2)

        if total_len == 0:
            return float(0)

        return self.find_median(nums1, nums2, midpoint)
