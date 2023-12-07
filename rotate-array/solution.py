from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        removed_values = {}

        for index in range(len(nums)):
          target_index = (index + k) % len(nums)
          target_value = nums[target_index]

          if index in removed_values:
            current_value = removed_values.pop(index)
          else:
            current_value = nums[index]

          nums[target_index] = current_value
          removed_values[target_index] = target_value
