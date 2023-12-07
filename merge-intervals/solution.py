from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        final_intervals = []
        checked_interval_indexes = []

        intervals.sort()

        for curr_index, curr_interval in enumerate(intervals):
            if curr_index in checked_interval_indexes:
                continue

            checked_interval_indexes.append(curr_index)
            interval_start = curr_interval[0]
            interval_end = curr_interval[1]

            for comp_index, comp_interval in enumerate(intervals[curr_index + 1 :]):
                true_comp_index = comp_index + curr_index + 1

                # comp_interval is encapsulated by curr_interval
                if comp_interval[0] >= interval_start and comp_interval[1] <= interval_end:
                    checked_interval_indexes.append(true_comp_index)

                elif comp_interval[0] <= interval_start:
                    # curr_interval is encapsulated by comp_interval
                    if comp_interval[1] >= interval_end:
                        interval_start = comp_interval[0]
                        interval_end = comp_interval[1]
                        checked_interval_indexes.append(true_comp_index)

                    # comp_interval overlaps with lower half of curr_interval
                    elif comp_interval[1] >= interval_start:
                        interval_start = comp_interval[0]
                        checked_interval_indexes.append(true_comp_index)

                # comp_interval overlaps with upper half of curr_interval
                elif comp_interval[1] >= interval_end and comp_interval[0] <= interval_end:
                    interval_end = comp_interval[1]
                    checked_interval_indexes.append(true_comp_index)
            
            final_intervals.append([interval_start, interval_end])

        return final_intervals
