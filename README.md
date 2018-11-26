# array-partitionable

Utility to check whether the list is partitionable or not. A partitioned list is one
where it can be split into 2 lists with equal sum.

This utility follows two steps:
1) Return False if the total sum of the array is odd value.
2) If value is even, with the help of hashmap algorithm find subarray whose sum equals to total_sum/2.
