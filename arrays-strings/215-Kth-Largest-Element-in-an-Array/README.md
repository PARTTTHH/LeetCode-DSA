# 215. Kth Largest Element in an Array

**LeetCode:** https://leetcode.com/problems/kth-largest-element-in-an-array/
**Difficulty:** Medium
**Pattern:** Arrays / Sorting

## Approach
Sort the array in descending order, then return the element at index k-1 
(since index 0 is the largest, index k-1 is the kth largest).

## Complexity
- Time: O(n log n) — dominated by the sort
- Space: O(1) extra (in-place sort)

## Notes
Straightforward reuse of sorting, similar to the sort-based approach used 
in Top K Frequent Elements. Clean re-entry problem after a week off for 
Travel Bharat submission.
