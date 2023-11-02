from typing import List


class Solution:
    def reverse_quicksort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        left_list = []
        right_list = []
        pivot = nums[0]

        for num in nums[1:]:
            if num > pivot:
                left_list.append(num)
            else:
                right_list.append(num)

        left_list = self.reverse_quicksort(left_list)
        right_list = self.reverse_quicksort(right_list)
        left_list.append(pivot)

        return left_list + right_list

    def findKthLargest(self, nums: List[int], target_index: int) -> int:
        sorted_nums = self.reverse_quicksort(nums)
        return sorted_nums[target_index - 1]
