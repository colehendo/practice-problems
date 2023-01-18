from typing import List


class Solution:
    def no_dupes_exist(self, point, points, index) -> bool:
        if point in points[index + 1 :]:
            return False
        return True

    def line_is_not_straight(self, points) -> bool:
        points_length = len(points)
        x_diff = points[1][0] - points[0][0]
        y_diff = points[1][1] - points[0][1]

        for index, point in enumerate(points[1:], start=1):
            if index == points_length - 1:
                break

            local_x_diff = points[index + 1][0] - point[0]
            if local_x_diff != x_diff:
                return True

            local_y_diff = points[index + 1][1] - point[1]
            if local_y_diff != y_diff:
                return True

        return False

    def check_for_boomerang(self, point, points, index):
        return self.check_for_boomerang_first_index(point, points, index)

    def check_for_boomerang_first_index(
        self, point, points: List[List[int]], index
    ) -> bool:
        self.check_for_boomerang = self.no_dupes_exist
        if not self.no_dupes_exist(point, points, index):
            return False

        return self.line_is_not_straight(points)

    def check_for_boomerang_remaining_indexes(
        self, point, points: List[List[int]], index
    ) -> bool:
        return self.no_dupes_exist(point, points, index)

    def is_boomerang(self, points: List[List[int]]) -> bool:
        for index, point in enumerate(points):
            boomerang_exists = self.check_for_boomerang(point, points, index)

            if not boomerang_exists:
                return False

        return True
