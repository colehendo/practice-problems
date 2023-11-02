Given an integer array `nums` and an integer `target_index`, return the `target_index` largest element in the array.

Note that it is the `target_index` largest element in the sorted order, not the `target_index` distinct element.

Can you solve it without sorting?

 

Example 1:

Input: `nums` = [3,2,1,5,6,4], `target_index` = 2
Output: 5
Example 2:

Input: `nums` = [3,2,3,1,2,4,5,5,6], `target_index` = 4
Output: 4
 

Constraints:

1 <= `target_index` <= `nums`.length <= 105
-104 <= `nums`[i] <= 104