from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], target_index: int) -> int:
        sorted_nums = sorted(nums, reverse=True)
        return sorted_nums[target_index - 1]
