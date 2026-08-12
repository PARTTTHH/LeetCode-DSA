# 167. Two Sum II - Input Array Is Sorted

**LeetCode:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
**Difficulty:** Medium
**Pattern:** Two Pointers

## Approach
Since the array is sorted, use two pointers starting at opposite ends 
(left=0, right=last index). Compute their sum: if it matches target, done. 
If too big, move right pointer left (shrinks sum, since right side has 
bigger values). If too small, move left pointer right (grows sum). Repeat 
until pointers meet or match is found.

## Complexity
- Time: O(n) — pointers move toward each other, at most n total steps combined
- Space: O(1) — only two index variables, satisfies problem's constant-space requirement

## Notes
First tried brute force (O(n²)) like Two Sum #1 — got Time Limit Exceeded, 
19/24 test cases, because it ignored the fact the array is sorted. Learned 
sorted input is a strong signal for Two Pointers. Initial two-pointer attempt 
had a broken while loop (used while...else incorrectly, and right started 
at -1 instead of len(numbers)-1) — fixed by starting right at the last 
valid index and using a proper while left < right loop with sum comparison 
inside.
