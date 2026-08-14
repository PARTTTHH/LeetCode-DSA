# 283. Move Zeroes

**LeetCode:** https://leetcode.com/problems/move-zeroes/
**Difficulty:** Easy
**Pattern:** Two Pointers

## Approach
`left` tracks the next position where a non-zero value belongs. Walk through 
the array once with `right`. Whenever a non-zero value is found at `right`, 
swap it with whatever's at `left`, then advance `left`. Zeros get naturally 
pushed toward the end as swaps happen, in-place, in one pass.

## Complexity
- Time: O(n) — single pass through the array
- Space: O(1) — in-place swaps, no extra structure

## Notes
First attempt used nums.pop(left) + nums.append(0) inside a while loop — 
passed the visible test case but failed 28/75 on submission. Root cause: 
popping shifts all later elements left by one, so a new zero can slide into 
the just-vacated index, but `left += 1` skips past it without re-checking. 
Also pop() is O(n) per call, making that approach O(n²) overall even where 
correct. Fixed with the standard two-pointer swap: only `left` moves forward 
(only when a non-zero is placed), `right` scans every index exactly once, 
no shifting/popping involved.

## Next step
Good case study in why mutating a list while indexing through it manually 
is risky — the list changes shape under the index. Worth remembering for 
future in-place problems.