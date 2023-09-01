from typing import List


class Solution:
    def first_missing_positive(self, nums: List[int]) -> int:
        nums = [num for num in nums if num > 0]
        nums.sort()

        if not nums or nums[0] != 1:
            return 1

        for index, num in enumerate(nums):
            try:
                if num != nums[index + 1] and num + 1 != nums[index + 1]:
                    return num + 1
            except IndexError:
                return num + 1

        return 1
