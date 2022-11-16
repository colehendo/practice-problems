from typing import List


class Solution:
    max_vol = 0
    left_index = 0
    right_index = 0

    def adjust_indexes(self, height: List[int], left_height: int, right_height: int):
        if left_height > right_height:
            self.right_index -= 1

            while (
                height[self.right_index] <= right_height
                and self.left_index < self.right_index
            ):
                self.right_index -= 1
        else:
            self.left_index += 1

            while (
                height[self.left_index] <= left_height
                and self.left_index < self.right_index
            ):
                self.left_index += 1

    def calculate_volume(self, height: List[int]):
        left_height = height[self.left_index]
        right_height = height[self.right_index]

        current_vol = min(left_height, right_height) * (
            self.right_index - self.left_index
        )
        if current_vol > self.max_vol:
            self.max_vol = current_vol

        self.adjust_indexes(height, left_height, right_height)

    def maxArea(self, height: List[int]) -> int:
        self.right_index = len(height) - 1

        while self.left_index < self.right_index:
            self.calculate_volume(height)

        return self.max_vol
