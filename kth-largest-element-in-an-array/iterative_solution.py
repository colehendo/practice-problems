from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], target_index: int) -> int:
        sorted_nums = []

        for num in nums:
            num_sorted = False
            for sorted_num_index, sorted_num in enumerate(sorted_nums):
                if num > sorted_num:
                    sorted_nums.insert(sorted_num_index, num)
                    num_sorted = True
                    break

            if not num_sorted and len(sorted_nums) < target_index:
                sorted_nums.append(num)

        return sorted_nums[target_index - 1]
