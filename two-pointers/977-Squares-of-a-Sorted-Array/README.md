# 977. Squares of a Sorted Array

**LeetCode:** https://leetcode.com/problems/squares-of-a-sorted-array/
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach
Since the array is sorted but can contain negatives, the largest square 
always comes from one of the two ends (most negative or most positive), 
never the middle. Use two pointers at opposite ends, compare their squares, 
place the bigger one at the END of the result array (filling backwards), 
and move that pointer inward. Repeat until pointers cross.

## Complexity
- Time: O(n) — single pass, pointers move toward each other
- Space: O(n) — new result array of the same size (required, since we can't 
  reliably square+sort in-place without extra space here)

## Notes
First tried brute force (square everything, then nums.sort()) just to test — 
surprisingly beat 94.97% runtime and 93.65% memory on LeetCode, despite 
being O(n log n) vs the two-pointer O(n). Turned out to be a good lesson: 
Python's built-in sort (Timsort) is C-optimized and very fast in practice, 
and LeetCode's runtime percentile is noisy — "passes fast" doesn't always 
mean "used the optimal algorithm." Still worth knowing the O(n) two-pointer 
version for interviews, since sorting-based answers usually invite a 
follow-up: "can you avoid sorting?"
