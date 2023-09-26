from typing import List


class Solution:
    def remove_element(self, nums: List[int], low_index: int, high_index: int, val: int) -> int:
        if low_index > high_index:
            return low_index

        if nums[low_index] == val:
            if nums[high_index] == val:
                high_index -= 1
                return self.remove_element(nums, low_index, high_index, val)

            nums[low_index] = nums[high_index]
            high_index -= 1
        low_index += 1

        return self.remove_element(nums, low_index, high_index, val)


    def removeElement(self, nums: List[int], val: int) -> int:
        low_index = 0
        high_index = len(nums) - 1

        non_val_count = self.remove_element(nums, low_index, high_index, val)

        return non_val_count
