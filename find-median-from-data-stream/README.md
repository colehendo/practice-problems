The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void add_num(int num) adds the integer num from the data stream to the data structure.
double find_median() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input
["MedianFinder", "add_num", "add_num", "find_median", "add_num", "find_median"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.add_num(1); // arr = [1]
medianFinder.add_num(2); // arr = [1, 2]
medianFinder.find_median(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.add_num(3); // arr[1, 2, 3]
medianFinder.find_median(); // return 2.0

Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling find_median.
At most 5 \* 104 calls will be made to add_num and find_median.
