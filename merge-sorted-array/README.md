You are given two integer arrays list_1 and list_2, sorted in non-decreasing order, and two integers list_1_elements and list_2_elements, representing the number of elements in list_1 and list_2 respectively.

Merge list_1 and list_2 into a single array sorted in non-decreasing order.

The final sorted array should be returned by the function. list_1 has a length of list_1_elements + list_2_elements, where the first list_1_elements elements denote the elements that should be merged, and the last list_2_elements elements are set to 0 and should be ignored. list_2 has a length of list_2_elements.

Example 1:

Input: list_1 = [1,2,3,0,0,0], list_1_elements = 3, list_2 = [2,5,6], list_2_elements = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from list_1.
Example 2:

Input: list_1 = [1], list_1_elements = 1, list_2 = [], list_2_elements = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: list_1 = [0], list_1_elements = 0, list_2 = [1], list_2_elements = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because list_1_elements = 0, there are no elements in list_1. The 0 is only there to ensure the merge result can fit in list_1.

Constraints:

list_1.length == list_1_elements + list_2_elements
list_2.length == list_2_elements
0 <= list_1_elements, list_2_elements <= 200
1 <= list_1_elements + list_2_elements <= 200
-109 <= list_1[i], list_2[j] <= 109
