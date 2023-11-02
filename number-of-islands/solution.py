from typing import List, Set, Tuple


class Solution:
    def __init__(self):
        self.adjacent_points = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def compile_island(self, point: Tuple[int, int]):
        self.points_visited.add(point)

        for adjacent_point in self.adjacent_points:
            new_point = (point[0] + adjacent_point[0], point[1] + adjacent_point[1])
            
            if new_point not in self.points_visited:
                try:
                    if self.grid[new_point[0]][new_point[1]] == "1":
                        self.compile_island(new_point)

                    self.points_visited.add(new_point)
                except IndexError:
                    # Main point is on edge of grid
                    continue

    def count_number_of_islands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.points_visited = set()
        number_of_islands = 0

        for row_index, _ in enumerate(grid):
            for column_index, value in enumerate(grid[row_index]):
                point = (row_index, column_index)
                if value == "1" and point not in self.points_visited:
                    number_of_islands += 1
                    self.compile_island(point)

        return number_of_islands

