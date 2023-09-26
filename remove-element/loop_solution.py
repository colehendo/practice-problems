from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        low_index = 0
        high_index = len(nums) - 1

        while low_index <= high_index:
            if nums[low_index] == val:
                if nums[high_index] == val:
                    high_index -= 1
                    continue

                nums[low_index] = nums[high_index]
                high_index -= 1
            low_index += 1

        return low_index
