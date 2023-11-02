from typing import List


class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        for index in reversed(range(2, len(nums))):
            if nums[index] == nums[index - 2]:
                del nums[index]
